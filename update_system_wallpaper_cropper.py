# This script is used to push the most up-to-date files from
# Launcher into frameworks' version of the WallpaperCropActivity
# (and supporting files)
# The framework versions have some small modifications that are
# necessary so do this with care
import os
import sys
src_dir = "WallpaperPicker/src/"
files = """
src/android.util/Pools.java
io.github.runassudo.launchert.gallery3d/util/IntArray.java
io.github.runassudo.launchert.gallery3d/common/Utils.java
io.github.runassudo.launchert.gallery3d/exif/ByteBufferInputStream.java
io.github.runassudo.launchert.gallery3d/exif/CountedDataInputStream.java
io.github.runassudo.launchert.gallery3d/exif/ExifData.java
io.github.runassudo.launchert.gallery3d/exif/ExifInterface.java
io.github.runassudo.launchert.gallery3d/exif/ExifInvalidFormatException.java
io.github.runassudo.launchert.gallery3d/exif/ExifModifier.java
io.github.runassudo.launchert.gallery3d/exif/ExifOutputStream.java
io.github.runassudo.launchert.gallery3d/exif/ExifParser.java
io.github.runassudo.launchert.gallery3d/exif/ExifReader.java
io.github.runassudo.launchert.gallery3d/exif/ExifTag.java
io.github.runassudo.launchert.gallery3d/exif/IfdData.java
io.github.runassudo.launchert.gallery3d/exif/IfdId.java
io.github.runassudo.launchert.gallery3d/exif/JpegHeader.java
io.github.runassudo.launchert.gallery3d/exif/OrderedDataOutputStream.java
io.github.runassudo.launchert.gallery3d/exif/Rational.java
io.github.runassudo.launchert.gallery3d/glrenderer/BasicTexture.java
io.github.runassudo.launchert.gallery3d/glrenderer/BitmapTexture.java
io.github.runassudo.launchert.gallery3d/glrenderer/GLCanvas.java
io.github.runassudo.launchert.gallery3d/glrenderer/GLES20Canvas.java
io.github.runassudo.launchert.gallery3d/glrenderer/GLES20IdImpl.java
io.github.runassudo.launchert.gallery3d/glrenderer/GLId.java
io.github.runassudo.launchert.gallery3d/glrenderer/GLPaint.java
io.github.runassudo.launchert.gallery3d/glrenderer/RawTexture.java
io.github.runassudo.launchert.gallery3d/glrenderer/Texture.java
io.github.runassudo.launchert.gallery3d/glrenderer/UploadedTexture.java
io.github.runassudo.launchert.photos/BitmapRegionTileSource.java
io.github.runassudo.launchert.photos/views/BlockingGLTextureView.java
io.github.runassudo.launchert.photos/views/TiledImageRenderer.java
io.github.runassudo.launchert.photos/views/TiledImageView.java
io.github.runassudo.launchert.gallery3d/common/BitmapUtils.java
io.github.runassudo.launchert/CropView.java
io.github.runassudo.launchert/WallpaperCropActivity.java
"""

if len(sys.argv) != 2:
    print "Usage: python update_sytem_wallpaper_cropper.py <framework_dir>"
    exit()
framework_dir = sys.argv[1] + "/packages/WallpaperCropper"
for file_path in files.split():
    file_path = src_dir + file_path
    dir = os.path.dirname(file_path)
    dir = dir.replace("launcher3", "wallpapercropper")
    dir = dir.replace(src_dir, "src/")
    cmd = 'cp %s %s/%s' % (file_path, framework_dir, dir)
    print cmd
    os.system(cmd)
