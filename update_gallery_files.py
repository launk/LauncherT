# This script is used to pull the most up-to-date files from
# Gallery into Launcher (we use some code from the Gallery
# source). The Launcher versions have some small modifications
# so do this with care, and be sure you are pulling from the
# latest version of Gallery
import os
import sys
files = """
src/android.util/Pools.java
src/io.github.runassudo.launchert.gallery3d/util/IntArray.java
src/io.github.runassudo.launchert.gallery3d/common/Utils.java
src/io.github.runassudo.launchert.gallery3d/exif/ByteBufferInputStream.java
src/io.github.runassudo.launchert.gallery3d/exif/CountedDataInputStream.java
src/io.github.runassudo.launchert.gallery3d/exif/ExifData.java
src/io.github.runassudo.launchert.gallery3d/exif/ExifInterface.java
src/io.github.runassudo.launchert.gallery3d/exif/ExifInvalidFormatException.java
src/io.github.runassudo.launchert.gallery3d/exif/ExifModifier.java
src/io.github.runassudo.launchert.gallery3d/exif/ExifOutputStream.java
src/io.github.runassudo.launchert.gallery3d/exif/ExifParser.java
src/io.github.runassudo.launchert.gallery3d/exif/ExifReader.java
src/io.github.runassudo.launchert.gallery3d/exif/ExifTag.java
src/io.github.runassudo.launchert.gallery3d/exif/IfdData.java
src/io.github.runassudo.launchert.gallery3d/exif/IfdId.java
src/io.github.runassudo.launchert.gallery3d/exif/JpegHeader.java
src/io.github.runassudo.launchert.gallery3d/exif/OrderedDataOutputStream.java
src/io.github.runassudo.launchert.gallery3d/exif/Rational.java
src/io.github.runassudo.launchert.gallery3d/glrenderer/BasicTexture.java
src/io.github.runassudo.launchert.gallery3d/glrenderer/BitmapTexture.java
src/io.github.runassudo.launchert.gallery3d/glrenderer/GLCanvas.java
src/io.github.runassudo.launchert.gallery3d/glrenderer/GLES20Canvas.java
src/io.github.runassudo.launchert.gallery3d/glrenderer/GLES20IdImpl.java
src/io.github.runassudo.launchert.gallery3d/glrenderer/GLId.java
src/io.github.runassudo.launchert.gallery3d/glrenderer/GLPaint.java
src/io.github.runassudo.launchert.gallery3d/glrenderer/RawTexture.java
src/io.github.runassudo.launchert.gallery3d/glrenderer/Texture.java
src/io.github.runassudo.launchert.gallery3d/glrenderer/UploadedTexture.java
src/io.github.runassudo.launchert.photos/BitmapRegionTileSource.java
src/io.github.runassudo.launchert.photos/views/BlockingGLTextureView.java
src/io.github.runassudo.launchert.photos/views/TiledImageRenderer.java
src/io.github.runassudo.launchert.photos/views/TiledImageView.java
src/io.github.runassudo.launchert.gallery3d/common/BitmapUtils.java
"""

if len(sys.argv) != 2:
    print "Usage: python update_gallery_files.py <gallery_dir>"
    exit()
gallery_dir = sys.argv[1]
for file_path in files.split():
    dir = os.path.dirname(file_path)
    if file_path.find('exif') != -1 or file_path.find('common') != -1:
        file_path = 'gallerycommon/' + file_path
    cmd = 'cp %s/%s WallpaperPicker/%s/' % (gallery_dir, file_path, dir)
    print cmd
    os.system(cmd)
