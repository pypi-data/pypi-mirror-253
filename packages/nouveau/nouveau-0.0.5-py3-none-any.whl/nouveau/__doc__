
# Art Nouveau Design Data

Public domain lazy-downloading data samples.

## Morris

This is a collection of designs by the famous Morris company artists of the 1800s.

# Format

 - image: image in numpy array or PyTorch tensor format
 - name: a common name for the design
 - year: initial year of design

# Example Use

    import nouveau
    data = nouveau.Morris()
    
    data.index.head()
    >> shows pandas dataframe head
    
    data[0]
    >> {'year': 1862,
    >>  'name': 'Fruit-Blue',
    >>  'filename': '1862-Fruit-Blue.jpg',
    >>  'image': array([[[254, 253, 249], ...
    
    data.show(1)
    >> <pyplot image>
    
    data.show('Fruit-Blue')
    >> <pyplot image>
    
    tensors = data.torch()
    tensors[0][0].shape
    >> torch.Size([3, 1987, 1586])


---
license: unlicense
task_categories:
- image-classification
pretty_name: Morris Co. Public Domain Art
size_categories:
- n<1K
---
