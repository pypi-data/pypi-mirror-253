from enum import Enum


class DatasetName(str, Enum):
    """
    The type of the dataset used for the model training
    """

    Imagenet = "ImageNet"
    CIFAR_10 = "CIFAR-10"
    Fashion_MNIST = "Fashion MNIST"
    COCO = "COCO"
    PASCAL_VOC = "PASCAL VOC"
    COCO_Segmentation = "COCO Segmentation"
    Cityscapes = "Cityscapes"
    Supervisely = "Supervisely"
    WoodScape = "WoodScape"
    WiderFace = "WiderFace"
    BDD100K = "BDD100K"
    OpenImage = "Open Image"
    LISA = "LISA Traffic Sign"
    DOTA = "DOTA"
    LFW = "LFW"
    CASIAWebFace = "CASIA-WebFace"
    Kinetics = "Kinetics"
    MaskedFaceNet = "MaskedFaceNet"
    ADE20K = "ADE20K"
    LVIS = "LVIS"
    Other = "Other"
    Empty = ""
