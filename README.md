## 一个简单得到mcp用于控制aria2c
### 使用要求
需要aria2c 运行于16800端口，且需要开启rpc接口
```bash
aria2c --enable-rpc --rpc-listen-all=true --rpc-allow-origin-all=true  --rpc-listen-port=16800
```
或者可以使用`main.py`来运行 `main.py` 会自动安装运行`aria2c`
```bash
python main.py
```
