# average-image
A Python script to average pixels in an image.


## Usage
```
python average_image.py <input> <output> <radius> <iterations>
```
|Parameter|Description|
|---------|-----------|
|input|The input image|
|output|The output image|
|radius|The radius of pixels to sample for each point|
|iterations|How many iterations to perform|


## Example
```
python average_image.py example/input.jpg example/output.jpg 5 3
```

### Console output
```
Opened image of size 1920 x 1200 pixels
Converting data
100.00% complete
Applying transformation
Iteration 3 - 99.92% complete
Writing new image to "example/output.jpg"
Done!
```

### Input Image
![Input Image](https://github.com/igorefremov/average-image/raw/master/example/input.jpg)

### Output Image
![Output Image](https://github.com/igorefremov/average-image/raw/master/example/output.jpg)
