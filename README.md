# Trad_Simp

A transformation tool between traditional Chinese and simplified Chinese in Python.

There some limitations or bugs in Opencc (https://code.google.com/p/opencc/) or pyjft (https://code.google.com/p/pyjft/). So I integrate some codes and develop this transformation tool.

Function: Transform traditional Chinese to simplified Chinese or transform simplified Chinese to traditional Chinese.

Description: Use a traditional Chinese dictionary and a corresponding simplified Chinese dictionary.

Addition: If you find the tradition Chinese dictionary is insufficiency, you can add some words youself (remeber to add the corresponding simplified word in the simplified dictionary).

Advantages:
    1. It transforms a string or a file word by word, so the string or a file can include other languages' characters.
    2. It allows the mixing of traditional Chinese and simplified Chinese.

Acknowledgements:
    1. Detecting a unicode character whether is the Chinese characters, numbers, English, or other characters code gets from http://www.cppblog.com/sunrise/archive/2012/08/29/188654.html or http://hi.baidu.com/fenghua1893/item/d1a71d5ac47ffdcfd3e10cd1.
    2. Traditional Chinese dictionary and a corresponding Simplified chinese dictionary gets from http://forum.ubuntu.org.cn/viewtopic.php?f=70&t=164501.

by ShawnXUNJU.

The data is copyed from the https://github.com/ShawnXUNJU/TraditionalCh2SimplifiedCh, and same as the file "detecting_tools.py".

I add the file "t2s.py" and "setup.py". There is an example in the "t2s.py".

you can use command "python setup.py install" to install the package.

by czf.
