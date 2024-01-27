__all__ = [
    'MLIServer',
]

import asyncio

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass

import os
import json
import shlex
import argparse
import traceback
from weakref import WeakKeyDictionary
from typing import AsyncIterator, TypedDict, Optional, Required, Unpack

from aiohttp import web, WSMsgType
from huggingface_hub import try_to_load_from_cache

from .params import Message, LLMParams, LlamaCppParams, CandleParams


DEBUG = int(os.getenv('DEBUG', 0))


class MLIServer:
    host: str
    port: int
    timeout: float
    candle_path: str
    llama_cpp_path: str
    app: web.Application
    lock: asyncio.Lock
    ws_proc_map: WeakKeyDictionary


    def __init__(self,
                 host: str='0.0.0.0',
                 port=5000,
                 timeout: float=90.0,
                 candle_path: str | None=None,
                 llama_cpp_path: str | None=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.candle_path = candle_path
        self.llama_cpp_path = llama_cpp_path
        self.app = web.Application()
        self.lock = asyncio.Lock()
        self.ws_proc_map = WeakKeyDictionary()


    def _format_llama_cpp_cmd(self, kind: str, **kwargs: Unpack[LlamaCppParams]) -> str:
        cmd: list[str] | str = []
        
        if kind == 'main':
            prompt: str = kwargs['prompt']
            model: str = kwargs['model']
            model_id: str | None = kwargs.get('model_id')
            chatml: bool | None = bool(kwargs.get('chatml', False))
            n_predict: int = int(kwargs.get('n_predict', '-2'))
            ctx_size: int = int(kwargs.get('ctx_size', '2048'))
            batch_size: int = int(kwargs.get('batch_size', '512'))
            temp: float = float(kwargs.get('temp', '0.8'))
            n_gpu_layers: int = int(kwargs.get('n_gpu_layers', '0'))
            top_k: int = int(kwargs.get('top_k', '40'))
            top_p: float = float(kwargs.get('top_p', '0.9'))
            no_display_prompt: float = float(kwargs.get('no_display_prompt', True))
            split_mode: str | None = kwargs.get('split_mode')
            tensor_split: str | None = kwargs.get('tensor_split')
            main_gpu: int | None = kwargs.get('main_gpu')
            
            # shell_prompt
            shell_prompt: str = shlex.quote(prompt)

            # model_path
            if model_id:
                model_path = try_to_load_from_cache(repo_id=model_id, filename=model)
            else:
                model_path = model

            cmd.extend([
                f'{self.llama_cpp_path}/{kind}',
                '--model', model_path,
            ])

            if chatml:
                cmd.extend([
                    '--chatml',
                ])

            if no_display_prompt:
                cmd.extend([
                    '--no-display-prompt',
                ])

            if split_mode is not None:
                cmd.extend([
                    '--split-mode', split_mode,
                ])

            if tensor_split is not None:
                cmd.extend([
                    '--tensor-split', tensor_split,
                ])

            if main_gpu is not None:
                cmd.extend([
                    '--main-gpu', main_gpu,
                ])

            cmd.extend([
                '--n-predict', n_predict,
                '--ctx-size', ctx_size,
                '--batch-size', batch_size,
                '--temp', temp,
                '--n-gpu-layers', n_gpu_layers,
                '--top-k', top_k,
                '--top-p', top_p,
                '--simple-io',
                '--log-disable',
                '--prompt', shell_prompt,
            ])
        else:
            raise ValueError(f'Unsupported kind: {kind}')

        cmd = ' '.join(str(n) for n in cmd)
        return cmd


    def _format_candle_cmd(self, kind: str, **kwargs: Unpack[CandleParams]) -> str:
        cmd: list[str] | str = []
        
        if kind == 'phi':
            prompt: str = kwargs['prompt']
            model: str = kwargs['model']
            cpu: bool = bool(kwargs.get('cpu', False))
            temperature: int = float(kwargs.get('temperature', '0.8'))
            top_p: int = float(kwargs.get('top_p', '0.9'))
            sample_len: int = int(kwargs.get('sample_len', '100'))
            quantized: bool = bool(kwargs.get('quantized', False))

            # shell_prompt
            shell_prompt: str = shlex.quote(prompt)
            
            cmd.extend([
                f'{self.candle_path}/target/release/examples/phi',
            ])

            if cpu:
                cmd.extend([
                    '--cpu',
                ])

            cmd.extend([
                '--model', model,
                '--temperature', temperature,
                '--top-p', top_p,
                '--sample-len', sample_len,
            ])
            
            if quantized:
                cmd.extend([
                    '--quantized',
                ])

            cmd.extend([
                '--prompt', shell_prompt,
            ])
        elif kind == 'stable-lm':
            prompt: str = kwargs['prompt']
            model_id: str = kwargs.get('model_id', 'lmz/candle-stablelm-3b-4e1t')
            cpu: bool = bool(kwargs.get('cpu', False))
            temperature: int = float(kwargs.get('temperature', '0.8'))
            top_p: int = float(kwargs.get('top_p', '0.9'))
            sample_len: int = int(kwargs.get('sample_len', '100'))
            quantized: bool = bool(kwargs.get('quantized', False))
            use_flash_attn: bool = bool(kwargs.get('use_flash_attn', False))

            # shell_prompt
            shell_prompt: str = shlex.quote(prompt)
            
            cmd.extend([
                f'{self.candle_path}/target/release/examples/stable-lm',
            ])

            if cpu:
                cmd.extend([
                    '--cpu',
                ])

            cmd.extend([
                '--model-id', model_id,
                '--temperature', temperature,
                '--top-p', top_p,
                '--sample-len', sample_len,
            ])
            
            if quantized:
                cmd.extend([
                    '--quantized',
                ])
            
            if use_flash_attn:
                cmd.extend([
                    '--use-flash-attn',
                ])

            cmd.extend([
                '--prompt', shell_prompt,
            ])
        elif kind == 'llama':
            prompt: str = kwargs['prompt']
            model_id: str = kwargs.get('model_id')
            cpu: bool = bool(kwargs.get('cpu', False))
            temperature: int = float(kwargs.get('temperature', '0.8'))
            top_p: int = float(kwargs.get('top_p', '0.9'))
            sample_len: int = int(kwargs.get('sample_len', '100'))
            use_flash_attn: bool = bool(kwargs.get('use_flash_attn', False))

            # shell_prompt
            shell_prompt: str = shlex.quote(prompt)

            cmd.extend([
                f'{self.candle_path}/target/release/examples/llama',
            ])

            if cpu:
                cmd.extend([
                    '--cpu',
                ])

            if model_id:
                cmd.extend([
                    '--model-id', model_id
                ])

            cmd.extend([
                '--temperature', temperature,
                '--top-p', top_p,
                '--sample-len', sample_len,
            ])
            
            if use_flash_attn:
                cmd.extend([
                    '--use-flash-attn',
                ])

            cmd.extend([
                '--prompt', shell_prompt,
            ])
        elif kind == 'mistral':
            prompt: str = kwargs['prompt']
            model_id: str = kwargs.get('model_id')
            cpu: bool = bool(kwargs.get('cpu', False))
            temperature: int = float(kwargs.get('temperature', '0.8'))
            top_p: int = float(kwargs.get('top_p', '0.9'))
            sample_len: int = int(kwargs.get('sample_len', '100'))
            quantized: bool = bool(kwargs.get('quantized', False))
            use_flash_attn: bool = bool(kwargs.get('use_flash_attn', False))

            # shell_prompt
            shell_prompt: str = shlex.quote(prompt)

            cmd.extend([
                f'{self.candle_path}/target/release/examples/mistral',
            ])

            if cpu:
                cmd.extend([
                    '--cpu',
                ])

            if model_id:
                cmd.extend([
                    '--model-id', model_id
                ])

            cmd.extend([
                '--temperature', temperature,
                '--top-p', top_p,
                '--sample-len', sample_len,
            ])
            
            if quantized:
                cmd.extend([
                    '--quantized',
                ])

            if use_flash_attn:
                cmd.extend([
                    '--use-flash-attn',
                ])

            cmd.extend([
                '--prompt', shell_prompt,
            ])
        elif kind == 'quantized':
            prompt: str = kwargs['prompt']
            model: str = kwargs['model']
            model_id: str | None = kwargs.get('model_id')
            cpu: bool = bool(kwargs.get('cpu', False))
            temperature: int = float(kwargs.get('temperature', '0.8'))
            top_p: int = float(kwargs.get('top_p', '0.9'))
            sample_len: int = int(kwargs.get('sample_len', '100'))

            # shell_prompt
            shell_prompt: str = shlex.quote(prompt)

            if model_id:
                model_path = try_to_load_from_cache(repo_id=model_id, filename=model)
            else:
                model_path = model

            cmd.extend([
                f'{self.candle_path}/target/release/examples/quantized',
            ])

            if cpu:
                cmd.extend([
                    '--cpu',
                ])

            cmd.extend([
                '--model', model_path,
                '--temperature', temperature,
                '--top-p', top_p,
                '--sample-len', sample_len,
                '--prompt', shell_prompt,
            ])
        else:
            raise ValueError(f'Unsupported kind: {kind}')

        cmd = ' '.join(str(n) for n in cmd)
        return cmd


    def _format_cmd(self, msg: LLMParams):
        engine: str = msg['engine']
        cmd: str

        if engine == 'llama.cpp':
            cmd = self._format_llama_cpp_cmd(**msg)
        elif engine == 'candle':
            cmd = self._format_candle_cmd(**msg)
        else:
            raise ValueError(f'Unknown engine: {engine}')

        return cmd


    async def _run_shell_cmd(self, ws: web.WebSocketResponse | None, msg: LLMParams, cmd: str) -> AsyncIterator[str]:
        prompt: str = msg['prompt']
        stop: str = msg.get('stop', [])
        stdout: bytes = b''
        stderr: bytes = b''
        stdout_text: str = ''
        prev_buf: bytes
        buf: bytes
        print(f'[DEBUG] _run_shell_cmd {ws} {msg} {cmd}')

        stop_ngrams: str = []

        for n in stop:
            for i in range(1, len(n) + 1):
                ngram = n[:i]
                stop_ngrams.append(ngram)

        print(f'{stop_ngrams = }')
        ngram_found: bool = False
        min_enc_stop_len: int = min(len(n.encode()) for n in stop) if stop else -1
        max_enc_stop_len: int = max(len(n.encode()) for n in stop) if stop else -1
        print(f'{min_enc_stop_len = }')
        print(f'{max_enc_stop_len = }')

        async with self.lock:
            try:
                async with asyncio.timeout(self.timeout):
                    # create new proc for model
                    proc = await asyncio.create_subprocess_shell(
                        cmd,
                        stdout=asyncio.subprocess.PIPE,
                        stderr=asyncio.subprocess.PIPE,
                    )

                    # associate ws with proc
                    if ws is not None:
                        self.ws_proc_map[ws] = proc
                    
                    # read rest of tokens
                    buf = b''
                    prev_buf = b''
                    text: str = prev_buf.decode()
                    stopped: bool = False

                    while not proc.stdout.at_eof():
                        buf = await proc.stdout.read(256)
                        prev_buf += buf
                        stdout += buf

                        try:
                            text = prev_buf.decode()
                        except Exception as e:
                            print(f'[ERROR] buf.decode() exception: {e}')
                            continue

                        # check for stop words
                        if ngram_found:
                            skip = False

                            while len(prev_buf) < max_enc_stop_len:
                                skip = True
                                break

                            if skip:
                                await asyncio.sleep(0.1)
                                continue

                            ngram_found = False
                        else:
                            for n in stop_ngrams:
                                if n in text:
                                    print(f'[INFO] stop ngram word {n!r}')
                                    ngram_found = True
                                    break

                            if ngram_found:
                                await asyncio.sleep(0.1)
                                continue
                        
                        prev_buf = b''
                        stdout_text += text

                        for n in stop:
                            if n in stdout_text:
                                print(f'[INFO] stop word {n!r} found as one of {stop!r}')
                                
                                b = stdout_text.rfind(text)
                                e = stdout_text.rfind(n)
                                # print(f'{b = }')
                                # print(f'{e = }')

                                if b > e:
                                    b = e
                                    # print(f'{b = }')

                                text = stdout_text[b:e]
                                stopped = True
                                break

                        yield text

                        if stopped:
                            break

                        await asyncio.sleep(0.2)

                    if stopped:
                        print(f'[INFO] stop word, trying to kill proc: {proc}')

                        try:
                            proc.kill()
                            await proc.wait()
                            print('[INFO] proc kill [stop]')
                        except Exception as e:
                            print(f'[INFO] proc kill [stop]: {e}')
                    
                    # read stderr at once
                    stderr = await proc.stderr.read()
            except asyncio.TimeoutError as e:
                print(f'[ERROR] timeout, trying to kill proc: {proc}')

                try:
                    proc.kill()
                    await proc.wait()
                    print('[INFO] proc kill [timeout]')
                except Exception as e:
                    print(f'[INFO] proc kill [timeout]: {e}')
                    raise e
            
            proc = None
            stderr = '...' + stderr.decode()[-1024:]
            print('[DEBUG] stderr:')
            print(stderr)


    def _run_cmd(self, ws: web.WebSocketResponse | None, msg: LLMParams) -> AsyncIterator[str]:
        engine: str = msg['engine']
        kind: str = msg['kind']
        cmd: str = self._format_cmd(msg)
        res: AsyncIterator[str]
        assert engine in ('llama.cpp', 'candle')

        if (engine == 'llama.cpp' and 'model_id' in msg) or (engine == 'candle' and kind == 'quantized' and 'model_id' in msg):
            model_id = msg['model_id']
            model = msg['model']
            
            if model_id:
                # check if model exists
                model_path = try_to_load_from_cache(repo_id=model_id, filename=model)

                if not isinstance(model_path, str):
                    raise ValueError(f'Model missing: {model_path}')
                else:
                    print(f'[INFO] found model: {model_path}')
            else:
                # FIXME: check if model exists
                model_path = model

        res = self._run_shell_cmd(ws, msg, cmd)
        return res


    async def _api_1_0_text_completions(self, ws: web.WebSocketResponse, msg: LLMParams):
        async for chunk in self._run_cmd(ws, msg):
            if DEBUG:
                print(f'chunk: {chunk!r}')

            msg: dict = {'chunk': chunk}
            await ws.send_json(msg)

        await ws.close()


    def _convert_chat_to_text_message(self, msg: LLMParams) -> LLMParams:
        """
        messages_syntax: None, 'chatml', 'llama', 'zephyr'
        role: 'system', 'user', 'assistant' but also supports 'question', 'answer'
        """
        messages: list[Message] = msg['messages']
        messages_syntax: str = msg.get('messages_syntax')
        conversation_text: list[str] = []
        prompt: list[str] | str = []
        roles: list[str] = []

        if messages_syntax is None:
            for m in messages:
                # Expected: system, user, assistant
                m_role = m['role']
                
                if m_role not in roles:
                    roles.append(m_role)

                if m['role'] == 'system':
                    m_content = ' '.join(m['content'].splitlines())
                    conversation_text.append(m_content)
                    conversation_text.append('\n\n')
                else:
                    conversation_text.append(f'{m_role.capitalize()}: ')
                    conversation_text.append(m['content'])
                    conversation_text.append('\n')

            if m['role'] == 'user':
                conversation_text.append('Assistant: ')
            else:
                # other than last role and system
                other_roles = [r for r in roles if r not in ('system', m['role'])]

                if other_roles:
                    m_role = other_roles[0]
                    conversation_text.append(f'{m_role.capitalize()}: ')
        elif messages_syntax == 'chatml':
            for m in messages:
                # Expected: system, user, assistant
                # Supported: system, question, answer
                m_role = m['role']

                if m_role not in roles:
                    roles.append(m_role)

                conversation_text.append(f'<|im_start|>{m_role}\n')
                conversation_text.append(m['content'])
                conversation_text.append('<|im_end|>\n')

            if m['role'] == 'user':
                conversation_text.append('<|im_start|>assistant\n')
            else:
                # other than last role and system
                other_roles = [r for r in roles if r not in ('system', m['role'])]

                if other_roles:
                    m_role = other_roles[0]
                    conversation_text.append(f'<|im_start|>{m_role}\n')
        elif messages_syntax == 'llama':
            system_message_closed: bool = False

            for m in messages:
                m_role = m['role']

                if m_role not in roles:
                    roles.append(m_role)

                if m_role == 'system':
                    conversation_text.append('[INST] <<SYS>>\n')
                    conversation_text.append(m['content'])
                    conversation_text.append('\n<</SYS>>\n')
                elif m_role == 'user':
                    if system_message_closed:
                        conversation_text.append('[INST] ')
                        conversation_text.append(m['content'])
                        conversation_text.append(' [/INST]\n')
                    else:
                        conversation_text.append(m['content'])
                        conversation_text.append(' [/INST]\n')
                        system_message_closed = True
                elif m_role == 'assistant':
                    conversation_text.append(m['content'])
                    conversation_text.append('\n')
                else:
                    raise ValueError(f'Unknown role {m_role!r}')
        elif messages_syntax == 'zephyr':
            for m in messages:
                m_role = m['role']

                if m_role not in roles:
                    roles.append(m_role)

                conversation_text.append(f'<|{m_role}|>\n')
                conversation_text.append(m['content'])
                conversation_text.append('</s>\n')

            if m['role'] == 'user':
                conversation_text.append('<|assistant|>\n')
            else:
                # other than last role and system
                other_roles = [r for r in roles if r not in ('system', m['role'])]

                if other_roles:
                    m_role = other_roles[0]
                    conversation_text.append(f'<|{m_role}|>\n')
        elif messages_syntax == 'stablelm-2-zephyr-1_6b':
            for m in messages:
                m_role = m['role']

                if m_role not in roles:
                    roles.append(m_role)

                if m['role'] == 'system':
                    conversation_text.append(m['content'])
                else:
                    conversation_text.append(f'<|{m_role}|>\n')
                    conversation_text.append(m['content'])
                    conversation_text.append('<|endoftext|>\n')

            if m['role'] == 'user':
                conversation_text.append('<|assistant|>\n')
            else:
                # other than last role and system
                other_roles = [r for r in roles if r not in ('system', m['role'])]

                if other_roles:
                    m_role = other_roles[0]
                    conversation_text.append(f'<|{m_role}|>\n')
        else:
            raise ValueError(f'Unknown syntax: {messages_syntax}')

        prompt.extend(conversation_text)
        prompt = ''.join(prompt)
        chat_msg: LLMParams = {**msg, 'prompt': prompt}
        return chat_msg


    async def post_api_1_0_text_completions(self, request):
        data: LLMParams = await request.json()
        text: list[str] | str = []

        async for chunk in self._run_cmd(None, data):
            if DEBUG:
                print(f'chunk: {chunk!r}')

            text.append(chunk)

        text = ''.join(text)

        res: dict = {
            'output': text,
        }

        return web.json_response(res)


    async def post_api_1_0_chat_completions(self, request):
        data: LLMParams = await request.json()
        data = self._convert_chat_to_text_message(data)
        text: list[str] | str = []

        async for chunk in self._run_cmd(None, data):
            if DEBUG:
                print(f'chunk: {chunk!r}')

            text.append(chunk)

        text = ''.join(text)

        res: dict = {
            'output': text,
        }

        return web.json_response(res)


    async def get_api_1_0_text_completions(self, request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        print(f'[INFO] websocket openned: {ws}')
        
        try:
            async with asyncio.TaskGroup() as tg:
                async for msg in ws:
                    if msg.type == WSMsgType.PING:
                        await ws.pong(msg.data)
                    elif msg.type == WSMsgType.TEXT:
                        data: LLMParams = json.loads(msg.data)
                        coro = self._api_1_0_text_completions(ws, data)
                        task = tg.create_task(coro)
                    elif msg.type == WSMsgType.ERROR:
                        print(f'[ERROR] websocket closed with exception: {ws.exception()}')
        except ExceptionGroup as e:
            traceback.print_exc()
            print(f'[ERROR] websocket ExceptionGroup: {e}')
        except Exception as e:
            traceback.print_exc()
            print(f'[ERROR] TaskGroup Exception: {e}')

        if ws in self.ws_proc_map:
            proc = self.ws_proc_map.pop(ws)
            print(f'[INFO] proc: {proc}')

            try:
                proc.kill()
                await proc.wait()
                print('[INFO] proc kill [TaskGroup]')
            except Exception as e:
                print(f'[WARN] proc kill [TaskGroup]: {e}')
            finally:
                proc = None

        # close ws
        await ws.close()

        print(f'[INFO] websocket closed: {ws}')
        return ws


    async def get_api_1_0_chat_completions(self, request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        print(f'[INFO] websocket openned: {ws}')
        
        try:
            async with asyncio.TaskGroup() as tg:
                async for msg in ws:
                    if msg.type == WSMsgType.PING:
                        await ws.pong(msg.data)
                    elif msg.type == WSMsgType.TEXT:
                        data: LLMParams = json.loads(msg.data)
                        data = self._convert_chat_to_text_message(data)
                        coro = self._api_1_0_text_completions(ws, data)
                        task = tg.create_task(coro)
                    elif msg.type == WSMsgType.ERROR:
                        print(f'[ERROR] websocket closed with exception: {ws.exception()}')
                        break
        except ExceptionGroup as e:
            traceback.print_exc()
            print(f'[ERROR] websocket ExceptionGroup: {e}')
        except Exception as e:
            traceback.print_exc()
            print(f'[ERROR] TaskGroup Exception: {e}')

        if ws in self.ws_proc_map:
            proc = self.ws_proc_map.pop(ws)
            print(f'[INFO] proc: {proc}')

            try:
                proc.kill()
                await proc.wait()
                print('[INFO] proc kill [TaskGroup]')
            except Exception as e:
                print(f'[WARN] proc kill [TaskGroup]: {e}')
            finally:
                proc = None

        # close ws
        await ws.close()

        print(f'[INFO] websocket closed: {ws}')
        return ws


    def get_routes(self):
        return [
            web.post('/api/1.0/text/completions', self.post_api_1_0_text_completions),
            web.post('/api/1.0/chat/completions', self.post_api_1_0_chat_completions),
            web.get('/api/1.0/text/completions', self.get_api_1_0_text_completions),
            web.get('/api/1.0/chat/completions', self.get_api_1_0_chat_completions),
        ]


    def run(self):
        routes = self.get_routes()
        self.app.add_routes(routes)
        web.run_app(self.app, host=self.host, port=self.port)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='server', description='Python llama.cpp HTTP Server')
    parser.add_argument('--host', help='http server host', default='0.0.0.0')
    parser.add_argument('--port', help='http server port', default=5000, type=float)
    parser.add_argument('--timeout', help='llama.cpp timeout in seconds', default=300.0, type=float)
    parser.add_argument('--candle-path', help='candle directory path', default='~/candle')
    parser.add_argument('--llama-cpp-path', help='llama.cpp directory path', default='~/llama.cpp')
    cli_args = parser.parse_args()

    server = MLIServer(
        host=cli_args.host,
        port=cli_args.port,
        timeout=cli_args.timeout,
        candle_path=os.path.expanduser(cli_args.candle_path),
        llama_cpp_path=os.path.expanduser(cli_args.llama_cpp_path),
    )

    server.run()
