<div align="center">

<img alt="ouroboros" src="./images/banner1.png" width="800px" style="max-width: 100%;">

<br/>
<br/>

**Unofficial Hugging Face Text Generation Utility Package.**

**[OUROBOROS VERSION 0.0.1]**

</div>

### Install ouroboros-hf-text-gen-utils
*Simple installation from PyPI*

```bash
pip install ouroboros_hf_text_gen_utils
```

<details>
  <summary>Other installation options</summary>

<br>

*Install from github directly*

```bash
pip install git+https://github.com/VINUK0/Ouroboros-HF-TXT-GEN-UTILS.git
```

</details>

### [Supported Features]

✅ *ONNX model inferece support via hugging face.*

✅ *OPENVINO model inferece support via hugging face.*

✅ *NF8 (8bit) and NF4 (4bit) inferece support via hugging face.*

✅ *Better Transformers inferece support via hugging face.*

⚠️ *Hugging face is slowly dropping better transformers support since* ***(scaled_dot_product_attention)*** *is being added to pytorch nativly.*

✅ *Flash Attention 2 inferece support via hugging face*

⚠️ *Your GPU architecture need to be Ampere or higher for flash attention 2 to work.* ***(First Ampere based GPU is RTX 3080 as said by google bard.)***

<br>

### [Coming In The Future]

🚧 *Save and Load Conversations.*

🚧 *Export the conversation's to human readable multiple prompt formats to create datasets.*

🚧 *Print total params in the model (I am busy to do it right now.)*

<br>

### [Supported Prompting Format's]

✅ *Alpaca Version 1*

<details>
  <summary>Backend Style</summary>

```
You are an helpful ai assistant.

### Instruction:
What is a computer.

### Response:
A computer is a programmable machine that manipulates information: it takes data, processes it, and stores it. Think of it as a powerful calculator that can follow instructions to do almost anything!
```
</details>

<br>

✅ *Alpaca Version 2* ***(Self Proclaimed)***

<details>
  <summary>Backend Style</summary>

```
### Instruction:
You are an helpful ai assistant.

### Input:
What is a computer.

### Response:
A computer is a programmable machine that manipulates information: it takes data, processes it, and stores it. Think of it as a powerful calculator that can follow instructions to do almost anything!
```
</details>

<br>

✅ *ChatML*

<details>
  <summary>Backend Style</summary>

```
<|im_start|>system:
You are an helpful ai assistant.<|im_end|>

<|im_start|>user:
What is a computer.<|im_end|>

<|im_start|>assistant:
A computer is a programmable machine that manipulates information: it takes data, processes it, and stores it. Think of it as a powerful calculator that can follow instructions to do almost anything!<|im_end|>
```
</details>

<br>

✅ *Ouroboros* ***(Same as TinyLlama 1B format)***

<details>
  <summary>Backend Style</summary>

```
<|system|>
You are an helpful ai assistant.

<|user>
What is a computer.

<|model|>
A computer is a programmable machine that manipulates information: it takes data, processes it, and stores it. Think of it as a powerful calculator that can follow instructions to do almost anything!
```
</details>

<br>

✅ *Mixtral* ***(This format is confusing to me.)***

<details>
  <summary>Backend Style</summary>

```
[INST] What is a computer.

[/INST] A computer is a programmable machine that manipulates information: it takes data, processes it, and stores it. Think of it as a powerful calculator that can follow instructions to do almost anything!
```
</details>

<br>

### [How to basic]
⚠️ *Available dtype's are `F32`, `F16`, `BF16`.*

⚠️ *Use can run these using this too `accelerate launch your_file_name.py`*

⚠️ *`max_sys_prompt_length`, `max_prompt_length` and `max_hist_length` is mesured by letters not tokens.*

🛠️ *Simple Inferece*

<details>
  <summary>Code example</summary>

```python
from ouroboros_text_gen_utils import text_generation

api = text_generation(tokenizer_name="Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct",
                      model_name="Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct",
                      dtype="BF16")

history = []

system_prompt = """### Instruction:
You are an helpful ai assistant."""

history, output = api.inplace_alpaca_v2_style(history=history,
                                     system_prompt=system_prompt,
                                     prompt="What is a computer.",
                                     user_name="user",
                                     character_name="assistant",
                                     max_sys_prompt_length=2048,
                                     max_prompt_length=1024,
                                     max_hist_length=8096,
                                     max_new_tokens=256,
                                     min_new_tokens=10,
                                     top_p=0.8,
                                     top_k=50,
                                     temperature=0.5,
                                     repetition_penalty=1.1)

print(f"Model Generated Output: {output}")
```
</details>

<br>

🛠️ *8 bit and 4 bit inferece.*

⚠️ *When loading models in 8 bit or 4 bit make sure the dtype is either `F16` or `BF16`.*

<details>
  <summary>Code example</summary>

```python
from ouroboros_text_gen_utils import text_generation

api = text_generation(tokenizer_name="Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct",
                      model_name="Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct",
                      dtype="BF16", load_in_4bit=True)

# load_in_8bit=True can be also used.

history = []

system_prompt = """### Instruction:
You are an helpful ai assistant."""

history, output = api.inplace_alpaca_v2_style(history=history,
                                     system_prompt=system_prompt,
                                     prompt="What is a computer.",
                                     user_name="user",
                                     character_name="assistant",
                                     max_sys_prompt_length=2048,
                                     max_prompt_length=1024,
                                     max_hist_length=8096,
                                     max_new_tokens=256,
                                     min_new_tokens=10,
                                     top_p=0.8,
                                     top_k=50,
                                     temperature=0.5,
                                     repetition_penalty=1.1)

print(f"Model Generated Output: {output}")
```
</details>

<br>

🛠️ *Flash Attention 1.*

⚠️ *Use can use this with `load_in_4bit` or `load_in_8bit` too.*

⚠️ *I have found a error when trying to run the model with flash attention 1 on a T4 GPU in `BF16`. If that happens use `F16` instead.*

<details>
  <summary>Code example</summary>

```python
from ouroboros_text_gen_utils import text_generation

api = text_generation(tokenizer_name="Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct",
                      model_name="Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct",
                      dtype="BF16", flash_attention="flash_attention_1")

history = []

system_prompt = """### Instruction:
You are an helpful ai assistant."""

history, output = api.inplace_alpaca_v2_style(history=history,
                                     system_prompt=system_prompt,
                                     prompt="What is a computer.",
                                     user_name="user",
                                     character_name="assistant",
                                     max_sys_prompt_length=2048,
                                     max_prompt_length=1024,
                                     max_hist_length=8096,
                                     max_new_tokens=256,
                                     min_new_tokens=10,
                                     top_p=0.8,
                                     top_k=50,
                                     temperature=0.5,
                                     repetition_penalty=1.1)

print(f"Model Generated Output: {output}")
```

</details>

<br>

🛠️ *Flash Attention 2.*

⚠️ *Use can use this with `load_in_4bit` or `load_in_8bit` too.*

⚠️ *You need this package to run FA2 `pip install flash-attn --no-build-isolation`*

<details>
  <summary>Code example</summary>

```python
from ouroboros_text_gen_utils import text_generation

api = text_generation(tokenizer_name="Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct",
                      model_name="Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct",
                      dtype="BF16", flash_attention="flash_attention_2")

history = []

system_prompt = """### Instruction:
You are an helpful ai assistant."""

history, output = api.inplace_alpaca_v2_style(history=history,
                                     system_prompt=system_prompt,
                                     prompt="What is a computer.",
                                     user_name="user",
                                     character_name="assistant",
                                     max_sys_prompt_length=2048,
                                     max_prompt_length=1024,
                                     max_hist_length=8096,
                                     max_new_tokens=256,
                                     min_new_tokens=10,
                                     top_p=0.8,
                                     top_k=50,
                                     temperature=0.5,
                                     repetition_penalty=1.1)

print(f"Model Generated Output: {output}")
```

</details>

<br>

🛠️ *Onnx model.*

⚠️ *If you have a GPU change the onnx_execution_provider to `onnx_execution_provider="CUDAExecutionProvider"`.*

<details>
  <summary>Code example</summary>

```python
from ouroboros_text_gen_utils import text_generation

api = text_generation(tokenizer_name="example/onnx_model_1B",
                      model_name="example/onnx_model_1B",
                      onnx_model=True, onnx_execution_provider="CPUExecutionProvider")

history = []

system_prompt = """### Instruction:
You are an helpful ai assistant."""

history, output = api.inplace_alpaca_v2_style(history=history,
                                     system_prompt=system_prompt,
                                     prompt="What is a computer.",
                                     user_name="user",
                                     character_name="assistant",
                                     max_sys_prompt_length=2048,
                                     max_prompt_length=1024,
                                     max_hist_length=8096,
                                     max_new_tokens=256,
                                     min_new_tokens=10,
                                     top_p=0.8,
                                     top_k=50,
                                     temperature=0.5,
                                     repetition_penalty=1.1)

print(f"Model Generated Output: {output}")
```

</details>

<br>

🛠️ *OpenVino model.*

⚠️ *If you have a GPU avaliable it will try to run from it.*

<details>
  <summary>Code example</summary>

```python
from ouroboros_text_gen_utils import text_generation

api = text_generation(tokenizer_name="example/openvino_model_1B",
                      model_name="example/openvino_model_1B",
                      openvino_model=True)

history = []

system_prompt = """### Instruction:
You are an helpful ai assistant."""

history, output = api.inplace_alpaca_v2_style(history=history,
                                     system_prompt=system_prompt,
                                     prompt="What is a computer.",
                                     user_name="user",
                                     character_name="assistant",
                                     max_sys_prompt_length=2048,
                                     max_prompt_length=1024,
                                     max_hist_length=8096,
                                     max_new_tokens=256,
                                     min_new_tokens=10,
                                     top_p=0.8,
                                     top_k=50,
                                     temperature=0.5,
                                     repetition_penalty=1.1)

print(f"Model Generated Output: {output}")
```
</details>

<br>

🛠️ *Better Transformer.*

<details>
  <summary>Code example</summary>

```python
from ouroboros_text_gen_utils import text_generation

api = text_generation(tokenizer_name="example/openvino_model_1B",
                      model_name="example/openvino_model_1B",
                      better_transformers=True, dtype="BF16")

history = []

system_prompt = """### Instruction:
You are an helpful ai assistant."""

history, output = api.inplace_alpaca_v2_style(history=history,
                                     system_prompt=system_prompt,
                                     prompt="What is a computer.",
                                     user_name="user",
                                     character_name="assistant",
                                     max_sys_prompt_length=2048,
                                     max_prompt_length=1024,
                                     max_hist_length=8096,
                                     max_new_tokens=256,
                                     min_new_tokens=10,
                                     top_p=0.8,
                                     top_k=50,
                                     temperature=0.5,
                                     repetition_penalty=1.1)

print(f"Model Generated Output: {output}")
```
</details>

### [All the supported prompt functions]

```python
inplace_alpaca_style()
inplace_alpaca_v2_style()
inplace_chatml_style()
inplace_ouroboros_style()
inplace_mixtral_style()
```