Movie Renamer
=============
The application is currently incomplete:
 - There's no GUI.
 
 - There's no way to install the app (besides cloning the repository).

 - The renamer doesn't work on a significant portion of possible movie file names.
 
Examples
--------
```python
>>> from movie_renamer import rename
>>> rename('Back.To.The.Future.Part.II.1989.1080p.BluRay.X264-LCHD.mkv')
0: 'Back to the Future Part II (1989).mkv'
>>> rename('Inception.DVDRiP.XviD-ARROW.avi')
1: 'Inception (2010).avi'
>>> rename('Back.To.The.Future.Part.II.1989.DVDRip.DivX.AC3.iNTERNAL-FFM.avi')
2: 'Back to the Future Part II (1989).avi'
>>> rename('Kill Bill.2003.DVDRip.XviD-DiCE.avi')
3: 'Kill Bill: Vol. 1 (2003).avi'
>>> rename('Gladiator[Extended.Edition]DvDrip.AC3[Eng]-aXXo.avi')
4: 'Gladiator (2000).avi'
>>> rename('Pirates_of_the_Caribbean_The_Curse_of_the_Black_Pearl.720p.ESiR.mkv')
5: 'Pirates of the Caribbean: The Curse of the Black Pearl (2003).mkv'
>>> rename('Shutter.Island.2010.480p.BRRip.x264.DXVA.AC3-FLAWL3SS.mkv')
6: 'Shutter Island (2010).mkv'
>>> rename('Monty.Python.and.the.Holy.Grail.DVDivX-SCHIZO.avi')
7: 'Monty Python and the Holy Grail (1975).avi'
>>> rename('King.Kong.2005.DVDRip.DivX5.AC3.2CH-aXXo.avi')
8: 'King Kong (2005).avi'
>>> rename('The.Avengers.2012.DVDRip.XviD-NYDIC.avi')
9: 'The Avengers (2012).avi'
>>> rename('Pulp.Fiction.1994.720p.BluRay.x264-SiNNERS.mkv')
10: 'Pulp Fiction (1994).mkv'
>>> rename('aladdin disney')
11: 'Aladdin (1994)'
>>> rename('green mile')
12: 'The Green Mile (1999)'
>>> rename('theDarkKnightRises')
13: 'The Dark Knight Rises (2012)'
>>> rename('matrix 2')
14: 'The Matrix Reloaded (2003)'
>>> rename('no.country.for.old.man.mp4')
15: 'No Country for Old Men (2007).mp4'
>>> rename('The Big Lebowski [Eng][XviD][1998].avi')
16: 'The Big Lebowski (1998).avi'
```

More examples can be found in the tests.

Requirements
------------
 - Python 2.7
 - IMDbPY