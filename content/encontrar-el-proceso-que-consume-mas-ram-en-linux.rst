Encontrar el proceso que consume más ram en Linux
#################################################
:date: 2010-12-09 12:30
:author: aesptux
:category: Linux
:tags: conocer, consume, encontrar, Linux, mas, memoria, mucha, proceso, ram
:slug: encontrar-el-proceso-que-consume-mas-ram-en-linux

Hay varias formas de hacerlo, la primera sería utilizando awk y sort

    ::

        ps aux | awk '{print $2, $4, $11}' | sort -k2r | head -n 20

 

Esto nos mostraría algo así:

`|image0|`_

 

Otra forma sería utilizar el comando '**top**\ ' y pulsar la tecla '>',
así directamente nos lo ordenará por consumo de RAM.

`|image1|`_

 

Y la última forma es utilizar el comando '**htop**\ ' y de la misma
forma pulsar la tecla '>', pero aquí nos preguntará que es lo que
queremos ordenar:

 

`|image2|`_

 

 

Via: `Go2Linux`_

.. _|image3|: http://farm6.static.flickr.com/5009/5243716642_cc04e1cd71.jpg
.. _|image4|: http://farm6.static.flickr.com/5209/5243716646_da8d55f560_z.jpg
.. _|image5|: http://farm6.static.flickr.com/5282/5243716648_b1ca63a971_z.jpg
.. _Go2Linux: http://www.go2linux.org/linux/2010/12/how-find-which-process-eating-ram-memory-linux-858

.. |image0| image:: http://farm6.static.flickr.com/5009/5243716642_cc04e1cd71.jpg
.. |image1| image:: http://farm6.static.flickr.com/5209/5243716646_da8d55f560_z.jpg
.. |image2| image:: http://farm6.static.flickr.com/5282/5243716648_b1ca63a971_z.jpg
.. |image3| image:: http://farm6.static.flickr.com/5009/5243716642_cc04e1cd71.jpg
.. |image4| image:: http://farm6.static.flickr.com/5209/5243716646_da8d55f560_z.jpg
.. |image5| image:: http://farm6.static.flickr.com/5282/5243716648_b1ca63a971_z.jpg
