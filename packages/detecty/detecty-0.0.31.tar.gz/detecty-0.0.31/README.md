# Detecty
A Mobilenet based single car plate detection model.

## Installation
Currently detecty is intended to use on CPU machine (GPU support is coming soon).
To install detecty on a CPU run:

```
pip3 install detecty
pip3 install torch --index-url https://download.pytorch.org/whl/cpu
```

## Usage
### Command line
If you have a car image named `car.jpg`

![](https://i.imgur.com/qrHvGmj.jpg)

You can run `detecty car.jpg` and get the plate in `plate.jpg`

![](https://i.imgur.com/C6gnTim.jpg)

### Python
```python
from PIL import Image
from detecty.model import Detection

img = Image.open('car.jpg')
model = Detection()
res = model(img)
res.plate.save('plate.jpg')
```
