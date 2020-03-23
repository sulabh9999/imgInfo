# imgInfo - Show image information 

[![](https://img.shields.io/badge/python-3.5-brightgreen)]() [![](https://img.shields.io/badge/PILLOW-7.0-orange)](https://github.com/python-pillow/Pillow) [![](https://img.shields.io/badge/Linux%20build-passing-brightgreen)](https://github.com/python-pillow/Pillow)

Get all information of image, supported imges types are png, jpej, tif etc. Tool supports API and Command line interface.


### Installation
ImgInfo requires [Python 3.5](https://www.python.org/) to run.
Install the dependencies and devDependencies and start the server.
#### pip
```sh
$ pip install imgInfo 
```

#### python3
```sh
$ git clone https://github.com/sulabh9999/imgInfo.git
$ cd imgInfo
$ python3 setup.py install 
```

### Development

cli interface
```sh
$ imginfo image.jpg
Image: image.jpg
Width: 1024
Height: 1024
Bands: 4
```

python3 API
```python
import imgInfo.main as im
result = im.info('image.jpg')
print(result)
```

[pillow](https://pypi.org/project/Pillow/) - The framework used to read image


## Contributing
For improvement pull requests are wellcome.


### License
Apache


  
