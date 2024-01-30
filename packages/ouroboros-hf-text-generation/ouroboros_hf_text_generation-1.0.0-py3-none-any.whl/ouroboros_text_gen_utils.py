import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, AutoConfig, AutoModel
from accelerate import Accelerator
import torch
import io
from logical_print import logical_print
import sys
lprint = logical_print().lprint
accelerator = Accelerator()

class model_loader():
    def __init__(self, model_name : str = "microsoft/phi-2", hf_auth_token : str | bool = False, local_files_only : bool = False, use_safetensors : bool = None, dtype : str = "BF16", cache_dir : str | None = None, load_in_4bit : bool = False, load_in_8bit = False, flash_attention : str | None = None, better_transformers : bool = False, onnx_model : bool = False, openvino_model : bool = False, onnx_execution_provider : str = "CPUExecutionProvider", print_params : bool = False, debug : bool = False) -> None:
        self.dtype_match = {'F16' : torch.float16,
                            'BF16' : torch.bfloat16,
                            'F32' : torch.float32}
        
        self.native_flash_support = ["gpt_bigcode", "gpt_neo", "gpt_neox", "falcon", "llama", "llava", "mistral", "mixtral", "opt", "phi"]
        
        self.model_name = model_name
        self.hf_auth_token = hf_auth_token
        self.local_files_only = local_files_only
        self.use_safetensors = use_safetensors
        self.dtype = dtype
        self.cache_dir = cache_dir
        self.flash_attention = flash_attention
        self.better_transformers = better_transformers
        self.onnx_model = onnx_model
        self.openvino_model = openvino_model
        self.execution_provider = onnx_execution_provider
        self.print_params = print_params
        self.debug = debug
        self.load_in_4bit = load_in_4bit
        self.load_in_8bit = load_in_8bit
        
        
    def hf_normal_model(self) -> None:
        dtype_to_load = self.dtype_match.get(self.dtype, 0)
        
        if self.load_in_4bit or self.load_in_8bit:
            self.bnb_config = BitsAndBytesConfig(
                load_in_4bit=self.load_in_4bit,
                load_in_8bit=self.load_in_8bit,
                bnb_4bit_quant_type="nf4",
                bnb_8bit_quant_type="nf8",
                bnb_4bit_compute_dtype=dtype_to_load,
                bnb_8bit_compute_dtype=dtype_to_load
                )
        if not self.load_in_4bit and not self.load_in_8bit:
            self.bnb_config = None
        
        
        if transformers.__version__ >= "4.37.1":
            
            if not self.flash_attention:
                self.model = AutoModelForCausalLM.from_pretrained(pretrained_model_name_or_path=self.model_name, torch_dtype=dtype_to_load, cache_dir=self.cache_dir, token=self.hf_auth_token, local_files_only=self.local_files_only, use_safetensors=self.use_safetensors, quantization_config=self.bnb_config)
                self.model.eval()
                if not self.load_in_8bit and not self.load_in_4bit:
                    self.model = accelerator.prepare_model(model=self.model, evaluation_mode=True)
                
                if self.debug:
                    lprint(level='OK', c_class='Model_Loader', func='hf_normal_model', line=61, msg=f'Model loaded successfully.')
                
            if self.flash_attention == "flash_attention_2":
                self.model = AutoModelForCausalLM.from_pretrained(pretrained_model_name_or_path=self.model_name, torch_dtype=dtype_to_load, cache_dir=self.cache_dir, token=self.hf_auth_token, local_files_only=self.local_files_only, use_safetensors=self.use_safetensors, attn_implementation=self.flash_attention, quantization_config=self.bnb_config)
                self.model.eval()
                if not self.load_in_8bit and not self.load_in_4bit:
                    self.model = accelerator.prepare_model(model=self.model, evaluation_mode=True)
                
                if self.debug:
                    lprint(level='OK', c_class='Model_Loader', func='hf_normal_model', line=70, msg=f'Model loaded successfully.')
                
            if self.flash_attention == "flash_attention_1":
                self.model = AutoModelForCausalLM.from_pretrained(pretrained_model_name_or_path=self.model_name, torch_dtype=dtype_to_load, cache_dir=self.cache_dir, token=self.hf_auth_token, local_files_only=self.local_files_only, use_safetensors=self.use_safetensors, attn_implementation="sdpa", quantization_config=self.bnb_config)
                self.model.eval()
                if not self.load_in_8bit and not self.load_in_4bit:
                    self.model = accelerator.prepare_model(model=self.model, evaluation_mode=True)
                if self.debug:
                    lprint(level='OK', c_class='Model_Loader', func='hf_normal_model', line=78, msg=f'Model loaded successfully.')
        else:
            if self.debug:
                lprint(level='WARN', error_type="VERSION ERROR", c_class='Model_Loader', func='hf_normal_model', line=81, msg=f'Flash attention requires transformers version 4.37.1 or higher. But current version is {transformers.__version__}, loading the model without it.')
            
            self.model = AutoModelForCausalLM.from_pretrained(pretrained_model_name_or_path=self.model_name, torch_dtype=dtype_to_load, cache_dir=self.cache_dir, token=self.hf_auth_token, local_files_only=self.local_files_only, use_safetensors=self.use_safetensors, quantization_config=self.bnb_config) 
            self.model.eval()
            if not self.load_in_8bit and not self.load_in_4bit:
                self.model = accelerator.prepare_model(model=self.model, evaluation_mode=True)
            if self.debug:
                lprint(level='OK', c_class='Model_Loader', func='hf_normal_model', line=88, msg=f'Model loaded successfully.')
                
    def hf_bt_model(self) -> None:
        from optimum.bettertransformer import BetterTransformer
        dtype_to_load = self.dtype_match.get(self.dtype, 0)
        
        if self.load_in_4bit or self.load_in_8bit:
            self.bnb_config = BitsAndBytesConfig(
                load_in_4bit=self.load_in_4bit,
                load_in_8bit=self.load_in_8bit,
                bnb_4bit_quant_type="nf4",
                bnb_8bit_quant_type="nf8",
                bnb_4bit_compute_dtype=dtype_to_load,
                bnb_8bit_compute_dtype=dtype_to_load
                )
        if not self.load_in_4bit and not self.load_in_8bit:
            self.bnb_config = None
            
        self.model = AutoModelForCausalLM.from_pretrained(pretrained_model_name_or_path=self.model_name, torch_dtype=dtype_to_load, cache_dir=self.cache_dir, token=self.hf_auth_token, local_files_only=self.local_files_only, use_safetensors=self.use_safetensors, quantization_config=self.bnb_config)
        self.model = BetterTransformer.transform(model=self.model, keep_original_model=True)
        self.model.eval()
        if not self.load_in_8bit and not self.load_in_4bit:
            self.model = accelerator.prepare_model(model=self.model, evaluation_mode=True)
        if self.debug:
            lprint(level='OK', c_class='Model_Loader', func='hf_bt_model', line=112, msg=f'Model loaded successfully.')
            
    def hf_onnx_model(self) -> None:
        from optimum.onnxruntime import ORTModelForCausalLM
        if self.debug:
            lprint(level='OK', c_class='Model_Loader', func='hf_onnx_model', line=117, msg=f'Ignoring model dtype as onnx models work using the pre define configs.')
        
        self.model = ORTModelForCausalLM.from_pretrained(model_id=self.model_name, cache_dir=self.cache_dir, provider=self.execution_provider, use_io_binding=None, use_auth_token=self.hf_auth_token, local_files_only=self.local_files_only)
        self.model.eval()
        if self.debug:
            lprint(level='OK', c_class='Model_Loader', func='hf_onnx_model', line=122, msg=f'Model loaded successfully.')
    
    def hf_openvino_model(self) -> None:
        from optimum.intel import OVModelForCausalLM
        if self.debug:
            lprint(level='OK', c_class='Model_Loader', func='hf_onnx_model', line=127, msg=f'Ignoring model dtype as onnx models work using the pre define configs.')
        
        self.model = OVModelForCausalLM.from_pretrained(model_id=self.model_name, cache_dir=self.cache_dir, provider=self.execution_provider, use_io_binding=None, use_auth_token=self.hf_auth_token, local_files_only=self.local_files_only, load_in_8bit=self.load_in_8bit)
        self.model = accelerator.prepare_model(model=self.model, evaluation_mode=True)
        self.model.eval()
        if self.debug:
            lprint(level='OK', c_class='Model_Loader', func='hf_onnx_model', line=133, msg=f'Model loaded successfully.')
    
    def get_correct_model(self) -> None:
        if not self.onnx_model and not self.openvino_model and not self.better_transformers:
            self.hf_normal_model()
            return self.model
        
        if not self.onnx_model and self.openvino_model:
            self.hf_openvino_model()
            return self.model
        if not self.openvino_model and self.onnx_model:
            self.hf_onnx_model()
            return self.model
        
        if not self.onnx_model and not self.openvino_model and self.better_transformers:
            config = AutoConfig.from_pretrained(pretrained_model_name_or_path=self.model_name)
            if config.model_type in self.native_flash_support:
                lprint(level='OK', c_class='Model_Loader', func='get_correct_model', line=150, msg=f'No need for better transformers, {config.model_type} is nativly supported by hugging face.\nUsing the equivalent to better transformers instead. Please put better_transformers=False next time.')
                self.flash_attention = "flash_attention_1"
                self.hf_normal_model()
                return self.model
            else:
                if self.debug:
                    lprint(level='OK', c_class='Model_Loader', func='get_correct_model', line=156, msg=f'Model loaded successfully.')
                self.hf_bt_model()
                return self.model
            
            
class text_generation(model_loader):
    def __init__(self, tokenizer_name : str = "microsoft/phi-2", model_name : str = "microsoft/phi-2", hf_auth_token : str | bool = False, local_files_only : bool = False, use_safetensors : bool = None, dtype : str = "BF16", cache_dir : str | None = None, load_in_4bit : bool = False, load_in_8bit = False, flash_attention : str | None = None, better_transformers : bool = False, onnx_model : bool = False, openvino_model : bool = False, onnx_execution_provider : str = "CPUExecutionProvider", print_params : bool = False, debug : bool = False) -> None:
        super().__init__(model_name=model_name, hf_auth_token=hf_auth_token, local_files_only=local_files_only, use_safetensors=use_safetensors, dtype=dtype, cache_dir=cache_dir, load_in_4bit=load_in_4bit, load_in_8bit=load_in_8bit, flash_attention=flash_attention, better_transformers=better_transformers, onnx_model=onnx_model, openvino_model=openvino_model, onnx_execution_provider=onnx_execution_provider, print_params=print_params, debug=debug)
        
        self.tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path=tokenizer_name, cache_dir=cache_dir)
        self.model = super().get_correct_model()
        
    def inplace_alpaca_style(self, history : list = None, system_prompt : str | None = 'You are an helpful ai assistant', prompt : str = '', user_name : str | None = 'user', character_name : str | None = 'assistant', max_sys_prompt_length : int = 200, max_prompt_length : int = 100, max_hist_length : int = 400, max_new_tokens : int = 100, min_new_tokens : int = 10, top_p : float = 0.80, top_k : int = 50, temperature : float = 0.5, repetition_penalty : float = 1.0, early_stopping : bool = False, use_cache : bool = True, no_auto_reply : bool = False)-> tuple[list, str]:
        
        temp = io.StringIO()
        for past in history:
            temp.write(past['content'])
        
        past_history = temp.getvalue()
        temp.close()
        
        if user_name and character_name:
            history.append({'role' : 'user', 'content' : f'\n### Instruction:\n{user_name}:\n{prompt[:max_prompt_length]}'})
        else:
            history.append({'role' : 'user', 'content' : f'\n### Instruction:\n{prompt[:max_prompt_length]}'})
        
        
        if not system_prompt and not user_name and not character_name:
            encode = self.tokenizer.encode(text=f"{past_history[-max_hist_length:]}\n### Instruction:\n{prompt[:max_prompt_length]}\n### Response:\n", return_tensors='pt').to(accelerator.device)
        
        if system_prompt and not user_name and not character_name:
            encode = self.tokenizer.encode(text=f"{system_prompt[:max_sys_prompt_length]}\n{past_history[-max_hist_length:]}\n### Instruction:\n{prompt[:max_prompt_length]}\n### Response:\n", return_tensors='pt').to(accelerator.device)
            
        if system_prompt and user_name and character_name:
            encode = self.tokenizer.encode(text=f"{system_prompt[:max_sys_prompt_length]}\n{past_history[-max_hist_length:]}\n### Instruction:\n{user_name}:\n{prompt[:max_prompt_length]}\n### Response:\n{character_name}:\n", return_tensors='pt').to(accelerator.device)
            
            
        attention_mask = torch.ones_like(encode).to(accelerator.device)
        
        output = self.model.generate(inputs=encode,
                                     attention_mask=attention_mask,
                                     max_new_tokens=int(max_new_tokens),
                                     min_new_tokens=int(min_new_tokens),
                                     top_p=float(top_p),
                                     top_k=int(top_k),
                                     temperature=float(temperature),
                                     repetition_penalty=float(repetition_penalty),
                                     use_cache=bool(use_cache),
                                     pad_token_id=self.tokenizer.eos_token_id,
                                     early_stopping=bool(early_stopping),
                                     do_sample=True,)
        
        decode = self.tokenizer.decode(output[:, encode.shape[-1]:][0], skip_special_tokens=True)
        
        if no_auto_reply and user_name and character_name:
            find_repeat = decode.index(f'### Instruction:\n{user_name}:')
            decode = decode[:find_repeat]
        
        if no_auto_reply and not user_name and character_name:
            find_repeat = decode.index(f'### Instruction:')
            decode = decode[:find_repeat]
            
                
        decode = decode.replace('### Instruction:', '').replace('### Response:', '')
        
        if user_name and character_name:
            decode = decode.replace(f'### Instruction:\n{user_name}', '').replace(f'### Response:\n{character_name}', '').replace(f'{user_name}:', '').replace(f'{character_name}:', '').replace('AIBOT:', '').replace('AIBot:', '')
            
            
        if user_name and character_name:
            history.append({'role' : 'assistant', 'content' : f'\n### Response:\n{character_name}:\n{decode}'})
        else:
            history.append({'role' : 'assistant', 'content' : f'\n### Response:\n{decode}'})
        
        return history, decode
    
    def inplace_chatml_style(self, history : list = None, system_prompt : str = 'system:\nYou are an helpful ai assistant', prompt : str = '', user_name : str = 'user', character_name : str = 'assistant', max_sys_prompt_length : int = 200, max_prompt_length : int = 100, max_hist_length : int = 400, max_new_tokens : int = 100, min_new_tokens : int = 10, top_p : float = 0.80, top_k : int = 50, temperature : float = 0.5, repetition_penalty : float = 1.0, early_stopping : bool = False, use_cache : bool = True)-> tuple[list, str]:
        
        temp = io.StringIO()
        
        for past in history:
            temp.write(past['content'])
        
        past_history = temp.getvalue()
        temp.close()
        
        if user_name and character_name:
            history.append({'role' : 'user', 'content' : f'\n[INST]{user_name}:\n{prompt[:max_prompt_length]}[/INST]'})
        else:
            lprint(level='FATAL', error_type="FORMAT ERROR", c_class='text_generation', func='inplace_chatml_style', line=245, msg=f'Aw snap, you cannot use this prompt format without a user_name and character_name due to the style of the prompting format.')
            sys.exit(__status=5)
        
    
        if system_prompt and user_name and character_name:
            encode = self.tokenizer.encode(text=f"[INST]{system_prompt[:max_sys_prompt_length]}[/INST]{past_history[-max_hist_length:]}\n[INST]{user_name}:\n{prompt[:max_prompt_length]}[/INST]\n[INST]{character_name}:\n", return_tensors='pt').to(accelerator.device)
        else:
            lprint(level='FATAL', error_type="FORMAT ERROR", c_class='text_generation', func='inplace_chatml_style', line=252, msg=f'Aw snap, you cannot use this prompt format without a system prompt, user_name and character_name due to the style of the prompting format.')
            sys.exit(__status=1)
        
        attention_mask = torch.ones_like(encode).to(accelerator.device)
        
        output = self.model.generate(inputs=encode,
                                     attention_mask=attention_mask,
                                     max_new_tokens=int(max_new_tokens),
                                     min_new_tokens=int(min_new_tokens),
                                     top_p=float(top_p),
                                     top_k=int(top_k),
                                     temperature=float(temperature),
                                     repetition_penalty=float(repetition_penalty),
                                     use_cache=bool(use_cache),
                                     pad_token_id=self.tokenizer.eos_token_id,
                                     early_stopping=bool(early_stopping),
                                     do_sample=True,)
        
        decode = self.tokenizer.decode(output[:, encode.shape[-1]:][0], skip_special_tokens=True)
        
        decode = decode.replace(f'{user_name}:', '').replace(f'{character_name}:', '')
            
        history.append({'role' : 'assistant', 'content' : f'\n[INST]{character_name}:\n{decode}[/INST]'})
        
        return history, decode
    
    def inplace_alpaca_v2_style(self, history : list = None, system_prompt : str | None = '### Instruction:\nYou are an helpful ai assistant', prompt : str = '', user_name : str | None = 'user', character_name : str | None = 'assistant', max_sys_prompt_length : int = 200, max_prompt_length : int = 100, max_hist_length : int = 400, max_new_tokens : int = 100, min_new_tokens : int = 10, top_p : float = 0.80, top_k : int = 50, temperature : float = 0.5, repetition_penalty : float = 1.0, early_stopping : bool = False, use_cache : bool = True, no_auto_reply : bool = False)-> tuple[list, str]:
        
        temp = io.StringIO()
        
        for past in history:
            temp.write(past['content'])
        
        past_history = temp.getvalue()
        temp.close()
        
        if user_name and character_name:
            history.append({'role' : 'user', 'content' : f'\n### Input:\n{user_name}:\n{prompt[:max_prompt_length]}'})
        else:
            history.append({'role' : 'user', 'content' : f'\n### Input:\n{prompt[:max_prompt_length]}'})
        
        
        if not system_prompt and not user_name and not character_name:
            encode = self.tokenizer.encode(text=f"{past_history[-max_hist_length:]}\n### Input:\n{prompt[:max_prompt_length]}\n### Response:\n", return_tensors='pt').to(accelerator.device)
        
        if system_prompt and not user_name and not character_name:
            encode = self.tokenizer.encode(text=f"{system_prompt[:max_sys_prompt_length]}\n{past_history[-max_hist_length:]}\n### Input:\n{prompt[:max_prompt_length]}\n### Response:\n", return_tensors='pt').to(accelerator.device)
        
        if system_prompt and user_name and character_name:
            encode = self.tokenizer.encode(text=f"{system_prompt[:max_sys_prompt_length]}\n{past_history[-max_hist_length:]}\n### Input:\n{user_name}:\n{prompt[:max_prompt_length]}\n### Response:\n{character_name}:\n", return_tensors='pt').to(accelerator.device)
            
            
        attention_mask = torch.ones_like(encode).to(accelerator.device)
        
        output = self.model.generate(inputs=encode,
                                     attention_mask=attention_mask,
                                     max_new_tokens=int(max_new_tokens),
                                     min_new_tokens=int(min_new_tokens),
                                     top_p=float(top_p),
                                     top_k=int(top_k),
                                     temperature=float(temperature),
                                     repetition_penalty=float(repetition_penalty),
                                     use_cache=bool(use_cache),
                                     pad_token_id=self.tokenizer.eos_token_id,
                                     early_stopping=bool(early_stopping),
                                     do_sample=True)
        
        decode = self.tokenizer.decode(output[:, encode.shape[-1]:][0], skip_special_tokens=True)
        
        if no_auto_reply and user_name and character_name:
            find_repeat = decode.index(f'### Input:\n{user_name}:')
            decode = decode[:find_repeat]
        
        if no_auto_reply and not user_name and character_name:
            find_repeat = decode.index(f'### Input:')
            decode = decode[:find_repeat]
            
                
        
        decode = decode.replace('### Input:', '').replace('### Response:', '')
        
        if user_name and character_name:
            decode = decode.replace(f'### Input:\n{user_name}', '').replace(f'### Response:\n{character_name}', '').replace(f'{user_name}:', '').replace(f'{character_name}:', '').replace('AIBOT:', '').replace('AIBot:', '')
            
        
        if user_name and character_name:
            history.append({'role' : 'assistant', 'content' : f'\n### Response:\n{character_name}:\n{decode}'})
        else:
            history.append({'role' : 'assistant', 'content' : f'\n### Response:\n{decode}'})
        
        
        return history, decode
    
    def inplace_ouroboros_style(self, history : list = None, system_prompt : str | None = '<|system|>\nYou are an helpful ai assistant', prompt : str = '', user_name : str | None = 'user', character_name : str | None = 'assistant', max_sys_prompt_length : int = 200, max_prompt_length : int = 100, max_hist_length : int = 400, max_new_tokens : int = 100, min_new_tokens : int = 10, top_p : float = 0.80, top_k : int = 50, temperature : float = 0.5, repetition_penalty : float = 1.0, early_stopping : bool = False, use_cache : bool = True, no_auto_reply : bool = False)-> tuple[list, str]:
        
        temp = io.StringIO()
        
        for past in history:
            temp.write(past['content'])
        
        past_history = temp.getvalue()
        temp.close()
        
        
        if user_name and character_name:
            history.append({'role' : 'user', 'content' : f'\n<|user|>\n{user_name}:\n{prompt[:max_prompt_length]}'})
        else:
            history.append({'role' : 'user', 'content' : f'\n<|user|>\n{prompt[:max_prompt_length]}'})
        
        
        if not system_prompt and not user_name and not character_name:
            encode = self.tokenizer.encode(text=f"{past_history[-max_hist_length:]}\n<|user|>\n{prompt[:max_prompt_length]}\n<|model|>\n", return_tensors='pt').to(accelerator.device)
        
        if system_prompt and not user_name and not character_name:
            encode = self.tokenizer.encode(text=f"{system_prompt[:max_sys_prompt_length]}{past_history[-max_hist_length:]}\n<|user|>\n{prompt[:max_prompt_length]}\n<|model|>\n", return_tensors='pt').to(accelerator.device)
            
        if system_prompt and user_name and character_name:
            encode = self.tokenizer.encode(text=f"{system_prompt[:max_sys_prompt_length]}{past_history[-max_hist_length:]}\n<|user|>\n{user_name}:\n{prompt[:max_prompt_length]}\n<|model|>\n{character_name}:\n", return_tensors='pt').to(accelerator.device)
            
        
        attention_mask = torch.ones_like(encode).to(accelerator.device)
        
        output = self.model.generate(inputs=encode,
                                     attention_mask=attention_mask,
                                     max_new_tokens=int(max_new_tokens),
                                     min_new_tokens=int(min_new_tokens),
                                     top_p=float(top_p),
                                     top_k=int(top_k),
                                     temperature=float(temperature),
                                     repetition_penalty=float(repetition_penalty),
                                     use_cache=bool(use_cache),
                                     pad_token_id=self.tokenizer.eos_token_id,
                                     early_stopping=bool(early_stopping),
                                     do_sample=True)
        
        decode = self.tokenizer.decode(output[:, encode.shape[-1]:][0], skip_special_tokens=True)
        
        if no_auto_reply and user_name and character_name:
            find_repeat = decode.index(f'<|user|>\n{user_name}:')
            decode = decode[:find_repeat]
        
        if no_auto_reply and not user_name and character_name:
            find_repeat = decode.index(f'<|user|>')
            decode = decode[:find_repeat]
            
                
        decode = decode.replace('<|user|>', '').replace('<|model|>', '')
        
        if user_name and character_name:
            decode = decode.replace(f'<|user|>\n{user_name}', '').replace(f'<|model|>\n{character_name}', '').replace(f'{user_name}:', '').replace(f'{character_name}:', '').replace('AIBOT:', '').replace('AIBot:', '')
            
        if user_name and character_name:
            history.append({'role' : 'assistant', 'content' : f'\n<|model|>\n{character_name}:\n{decode}'})
        else:
            history.append({'role' : 'assistant', 'content' : f'\n<|model|>\n{decode}'})
        
        return history, decode

    def inplace_mixtral_style(self, history : list = None, system_prompt : str = 'system:\nYou are an helpful ai assistant', prompt : str = '', user_name : str = 'user', character_name : str = 'assistant', max_sys_prompt_length : int = 200, max_prompt_length : int = 100, max_hist_length : int = 400, max_new_tokens : int = 100, min_new_tokens : int = 10, top_p : float = 0.80, top_k : int = 50, temperature : float = 0.5, repetition_penalty : float = 1.0, early_stopping : bool = False, use_cache : bool = True)-> tuple[list, str]:
        
        temp = io.StringIO()
        
        for past in history:
            temp.write(past['content'])
        
        past_history = temp.getvalue()
        temp.close()
        
        if user_name and character_name:
            history.append({'role' : 'user', 'content' : f'\n[INST]{user_name}:\n{prompt[:max_prompt_length]}[/INST]'})
        else:
            lprint(level='FATAL', error_type="FORMAT ERROR", c_class='text_generation', func='inplace_mixtral_style', line=423, msg=f'Aw snap, you cannot use this prompt format without a user_name and character_name due to the style of the prompting format.')
            sys.exit(__status=5)
        
    
        if system_prompt and user_name and character_name:
            encode = self.tokenizer.encode(text=f"[INST]{system_prompt[:max_sys_prompt_length]}[/INST]{past_history[-max_hist_length:]}\n[INST]{user_name}:\n{prompt[:max_prompt_length]}[/INST]\n[INST]{character_name}:\n", return_tensors='pt').to(accelerator.device)
        else:
            lprint(level='FATAL', error_type="FORMAT ERROR", c_class='text_generation', func='inplace_mixtral_style', line=430, msg=f'Aw snap, you cannot use this prompt format without a system prompt, user_name and character_name due to the style of the prompting format.')
            sys.exit(__status=1)
        
        attention_mask = torch.ones_like(encode).to(accelerator.device)
        
        output = self.model.generate(inputs=encode,
                                     attention_mask=attention_mask,
                                     max_new_tokens=int(max_new_tokens),
                                     min_new_tokens=int(min_new_tokens),
                                     top_p=float(top_p),
                                     top_k=int(top_k),
                                     temperature=float(temperature),
                                     repetition_penalty=float(repetition_penalty),
                                     use_cache=bool(use_cache),
                                     pad_token_id=self.tokenizer.eos_token_id,
                                     early_stopping=bool(early_stopping),
                                     do_sample=True,)
        
        decode = self.tokenizer.decode(output[:, encode.shape[-1]:][0], skip_special_tokens=True)
        
        decode = decode.replace(f'{user_name}:', '').replace(f'{character_name}:', '')
            
        history.append({'role' : 'assistant', 'content' : f'\n[INST]{character_name}:\n{decode}[/INST]'})
        
        return history, decode