import abc

class Resetable(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass: type) -> bool:
        return hasattr(__subclass,'reset') and callable(__subclass.reset) or NotImplemented
    
    @abc.abstractmethod
    def reset(self, *args,**kwargs) -> None:
        """Reset the object"""
        raise NotImplementedError

 
class Updatable(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass: type) -> bool:
        return hasattr(__subclass,'update') and callable(__subclass.update) or NotImplemented
    

    @abc.abstractmethod 
    def update(self,*args,**kwargs) -> None:
        # Update the object according to a new configuration
        raise NotImplementedError


class Detector(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass: type) -> bool:
        return hasattr(__subclass,'detect') and callable(__subclass.detect) or NotImplemented
    

    @abc.abstractmethod 
    def detect(self,*args,**kwargs) -> None:
        # Localize and classify the objects in the image or video
        raise NotImplementedError



class Tracker(metaclass=abc.ABCMeta):
    
    @classmethod
    def __subclasshook__(cls, __subclass: type) -> bool:
        return hasattr(__subclass,'track') and callable(__subclass.track) or NotImplemented
    

    @abc.abstractmethod 
    def track(self,*args,**kwargs) -> None:
        # Track objects from an image or a video
        raise NotImplementedError

class Localizer(metaclass=abc.ABCMeta):
    """
    The difference between the Localizer and the Detector is that the localizer does not classify the discoveries that it provides, while the detector does. 
    """
    @classmethod
    def __subclasshook__(cls, __subclass: type) -> bool:
        return hasattr(__subclass,'localize') and callable(__subclass.localize) or NotImplemented
    

    @abc.abstractmethod 
    def localize(self,*args,**kwargs) -> None:
        # Localize objects from an image or a video, should only return bounding boxes, without any classes.
        raise NotImplementedError


class Classifier(metaclass=abc.ABCMeta):
    
    @classmethod
    def __subclasshook__(cls, __subclass: type) -> bool:
        return hasattr(__subclass,'classify') and callable(__subclass.classify) or NotImplemented
    

    @abc.abstractmethod 
    def classify(self,*args,**kwargs) -> None:
        # Classify objects from an image or a video
        raise NotImplementedError




    

    
