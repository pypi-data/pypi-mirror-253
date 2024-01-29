### GGUF model caller
[<img src="https://raw.githubusercontent.com/calcuis/gguf-connector/master/gguf.gif" width="128" height="128">](https://github.com/calcuis/gguf-connector/blob/main/gguf.gif)

This package is a GGUF (GPT-Generated Unified Format) file/model caller.
#### install the caller via pip/pip3 (once only):
```
pip install callgg
```
#### update the caller (if not in the latest version) by:
```
pip install callgg --upgrade
```
### new feature(s) in the latest version
Connector selection menu and flag -v or --version
### user manual
This is a cmd-based (command line) package, you can find the user manual by adding the flag -h or --help.
```
callgg -h
```
### graphical user interface (GUI) caller
A basic GUI to interact with a chat model for generating responses (recommanded).
#### call cpp connector:
```
callgg cpp
``` 
#### call c connector:
```
callgg c
```
### command line interface (CLI) caller
A simple CLI input also provided for expert/advanced user(s).
#### call gpp connector:
```
callgg gpp
```
#### call g connector:
```
callgg g
```
GGUF file(s) in the same directory will automatically be detected by the caller, hence, a selection menu will be shown in the console as below.

[<img src="https://raw.githubusercontent.com/calcuis/chatgpt-model-selector/master/demo.gif" width="350" height="280">](https://github.com/calcuis/chatgpt-model-selector/blob/main/demo.gif)
[<img src="https://raw.githubusercontent.com/calcuis/chatgpt-model-selector/master/demo1.gif" width="350" height="280">](https://github.com/calcuis/chatgpt-model-selector/blob/main/demo1.gif)

#### sample model(s) available to download (try out)
For general purpose
https://huggingface.co/calcuis/chat/blob/main/chat.gguf

For coding
https://huggingface.co/calcuis/code_mini/blob/main/code.gguf

For health/medical advice
https://huggingface.co/calcuis/medi_mini/blob/main/medi.gguf

***those are all experimental models; no guarantee on quality