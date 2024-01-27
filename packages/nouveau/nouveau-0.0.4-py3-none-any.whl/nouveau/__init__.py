
import pandas as _pd
import os as _os
import urllib.request as _request
from skimage import io as _io
import matplotlib.pyplot as _plt
from pathlib import Path as _Path
from PIL import Image as _Image

with open(_os.path.abspath(_os.path.dirname(__file__))+'/__doc__','r') as _f:
    __doc__ = _f.read()

# Ignore warnings
import warnings as _warnings
_warnings.filterwarnings("ignore")

_plt.ion()   # interactive mode

class Morris():
    _storage_csv='morris.csv'
    _storage_jpg='jpgs'
    def __init__(self,root=_Path(__file__).parent,transform=False):
        self.storage_path = _Path(root)
        self.transform = transform
        self.index = _pd.read_csv(self.storage_path / self._storage_csv)
        self._self_validate()

    def to_torch(self):
        import torch
        from torchvision import transforms

        class MorrisDataset(torch.utils.data.Dataset,Morris):

            def __init__(self,root=_Path(__file__).parent,transform=False):
                super().__init__()

            def show(self,idx):
                name=None
                if isinstance(idx,str):
                    if idx in self.index.name.values:
                        idx = self.index.index[self.index.name==idx][0]
                        idx = int(idx)
                        name = self.index.name[idx]
                        print(f"found item {idx} by name {name}")
                    else:
                        raise ValueError('item name not found')
                if isinstance(idx,int):
                    name = self.index.name[idx]
                    _plt.title(name)
                    _plt.imshow(transforms.ToPILImage()(self.__getitem__(idx)[0]))
                else:
                    _plt.imshow(transforms.ToPILImage()(idx))

            def __getitem__(self,idx):
                item = self.index.iloc[idx].to_dict()
                image = _io.imread(self.storage_path / self._storage_jpg / self.index.iloc[idx].filename)
                image = torch.tensor(image).permute(2,0,1)
                if self.transform:
                    image = self.transform(image)

                item = [image,item['name'],item['year']]
                return item

        return MorrisDataset(str(self.storage_path),self.transform)

    def __len__(self):
        return len(self.index)

    def __getitem__(self,idx):
        item = self.index.iloc[idx].to_dict()
        image = _io.imread(self.storage_path / self._storage_jpg / self.index.iloc[idx].filename)

        if self.transform:
            image = self.transform(image)

        item['image'] = image
        return item

    def show(self,idx):
        if isinstance(idx,str):
            if idx in self.index.name.values:
                idx = self.index.index[self.index.name==idx][0]
                idx = int(idx)
                name = self.index.name[idx]
                print(f"found item {idx} by name {name}")
            else:
                raise ValueError('item name not found')
        if isinstance(idx,int):
            _item = self.__getitem__(idx)
            image = _item['image']
            name  = _item['name']
            _plt.title(name)
            _plt.imshow(_Image.fromarray(image))
        else:
            try:
                _plt.imshow(_Image.fromarray(idx))
            except AttributeError:
                _plt.imshow(_Image.fromarray(idx.permute(1,2,0).numpy()))

    def _self_validate(self):
        """try loading each image in the dataset"""
        allgood=True
        for filename in self.index.filename.values:
            _file = _Path(self.storage_path / self._storage_jpg / filename)
            if _file.is_file():
                continue
            else:
                allgood=False
                _os.makedirs(_file.parent,exist_ok=True)
                try:
                    print(f"downloading {filename}")
                    url = f"https://huggingface.co/datasets/dactylroot/morris/resolve/main/jpgs/{filename}"
                    _request.urlretrieve(url,_file)
                except:
                    print(f"couldn't load {filename}")
        if allgood:
            print(f"{len(self)} images present.")
            
class Deframe(object):
    """check for uniform color boundaries on edges of input and crop them away"""
    from torch import Tensor

    def __init__(self,aggressive=False,maxPixelFrame=20):
        self.alpha = 0.1 if aggressive else 0.01
        self.maxPixelFrame = maxPixelFrame

    def _map2idx(self,frameMap):
        try:
            return frameMap.tolist().index(False)
        except ValueError:
            return self.maxPixelFrame

    def _Border(self,img: Tensor):
        """ take greyscale Tensor
            return left,right,top,bottom border size identified """
        import torch
        top = left = right = bottom = 0

        # expected image variance
        hvar,wvar = torch.mean(torch.var(img,dim=0)), torch.mean(torch.var(img,dim=1))

        # use image variance and alpha to identify too-uniform frame borders
        top = torch.var(img[:self.maxPixelFrame,:],dim=1) < wvar*(1+self.alpha)
        top = self._map2idx(top)

        bottom = torch.var(img[-self.maxPixelFrame:,:],dim=1) < wvar*(1+self.alpha)
        bottom = self._map2idx(bottom)

        left = torch.var(img[:,:self.maxPixelFrame],dim=0) < hvar*(1+self.alpha)
        left = self._map2idx(left)

        right = torch.var(img[:,-self.maxPixelFrame:],dim=0) < hvar*(1+self.alpha)
        right = self._map2idx(right)

        return (top,bottom,right,left)

    def __call__(self,img: Tensor):
        import torchvision
        top,bottom,right,left = self._Border(torchvision.transforms.Grayscale()(img)[0])

        height = img.shape[1]-(top+bottom)
        width  = img.shape[2]-(left+right)

        print(f"t{top} b{bottom} l{left} r{right}")

        return torchvision.transforms.functional.crop(img,top,left,height,width)
