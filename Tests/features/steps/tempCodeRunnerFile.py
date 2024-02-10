# This should be used when running inside a yml file through CI pipeline

from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024, 768))
display.start()