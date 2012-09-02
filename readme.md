Movie Renamer
=============
The application is currently incomplete:
 - There's no GUI and no way to install the app (besides copying the code).

 - The renamer doesn't work on a significant portion of possible movie file names.
 
Examples
--------
Examples can be found in the tests. 

The following is a snippet of the movie renamer test data:

```python
filenames = \
{'Back.To.The.Future.Part.II.1989.1080p.BluRay.X264-LCHD.mkv': \
 'Back to the Future Part II (1989).mkv',
 'Inception.DVDRiP.XviD-ARROW.avi':
 'Inception (2010).avi',
 'Back.To.The.Future.Part.II.1989.DVDRip.DivX.AC3.iNTERNAL-FFM.avi':
 'Back to the Future Part II (1989).avi',
 'Kill Bill.2003.DVDRip.XviD-DiCE.avi':
 'Kill Bill: Vol. 1 (2003).avi',
 'Gladiator[Extended.Edition]DvDrip.AC3[Eng]-aXXo.avi':
 'Gladiator (2000).avi',
 'Pirates_of_the_Caribbean_The_Curse_of_the_Black_Pearl.720p.ESiR.mkv':
 'Pirates of the Caribbean: The Curse of the Black Pearl (2003).mkv',
 'Shutter.Island.2010.480p.BRRip.x264.DXVA.AC3-FLAWL3SS.mkv':
 'Shutter Island (2010).mkv',
 'Monty.Python.and.the.Holy.Grail.DVDivX-SCHIZO.avi':
 'Monty Python and the Holy Grail (1975).avi'}
```

The following function (successfully) tests the rename function on the above test data:

```python
def test_rename(self):
    for old_filename, new_filename in filenames.items():
        self.assertEqual(rename(old_filename), new_filename)
```