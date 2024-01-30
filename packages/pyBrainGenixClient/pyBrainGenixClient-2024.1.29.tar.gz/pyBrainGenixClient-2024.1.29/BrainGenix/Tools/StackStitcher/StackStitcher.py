# BrainGenix-NES
# AGPLv3

import os
import sys
import imageio

import PIL.Image
import PIL.ImageDraw



class SliceStitcher:

    def __init__(self, _Verbose:bool=False, _AddBorders:bool=False, _BorderSize_px:int=8, _LabelImages:bool=False, _MakeGif:bool=False):
        self.Verbose = _Verbose
        self.AddBorders = _AddBorders
        self.LabelImages = _LabelImages
        self.BorderSize_px = _BorderSize_px
        self.MakeGif = _MakeGif



    def StitchSlice(self, _DirectoryPath:str, _OutputDir:str, _FileNames:list):

        NumSlices = len(_FileNames)
        if (self.Verbose):
            print(f"    - Region Has {NumSlices} Slice(s)")

        if not os.path.exists(_OutputDir):
            os.mkdir(_OutputDir)


        # Keep Track Of List Of Slice Images For Gif (If Enabled)
        SliceFilenames:list = []

        for ThisSliceNumber in range(NumSlices):



            SortedFiles = os.listdir(_DirectoryPath + _FileNames[ThisSliceNumber])


            ReferenceImageSize = PIL.Image.open(_DirectoryPath + _FileNames[ThisSliceNumber] + "/" + SortedFiles[0]).size

            # Lists to hold X and Y values
            Xvalues = []
            Yvalues = []
            for File in SortedFiles:
                XVal:int = int(File.split("X")[0])
                YVal:int = int(File.split("_")[1].replace("Y.png", ""))
                if (not XVal in Xvalues):
                    Xvalues.append(XVal)
                if (not YVal in Yvalues):
                    Yvalues.append(YVal)




            # # Pair up the Xvalues and Y values into a list
            # Yvalues = sorted(Yvalues)
            # Xvalues = sorted(Xvalues)
            # XList_Without_Duplicates = []
            # YList_Without_Duplicates = []
            
            # for item in Xvalues:
            #     if item not in XList_Without_Duplicates:
            #         XList_Without_Duplicates.append(item)
            # for item in Yvalues:
            #     if item not in YList_Without_Duplicates:
            #         YList_Without_Duplicates.append(item)

            # YIncrements = (YList_Without_Duplicates[1] - YList_Without_Duplicates[0])
            # XIncrements = (XList_Without_Duplicates[1] - XList_Without_Duplicates[0])



            XTileCounter = len(Xvalues)
            YTileCounter = len(Yvalues)

            OutputImageSize = [ReferenceImageSize[0] * XTileCounter, ReferenceImageSize[1] * YTileCounter]
            if (self.AddBorders):
                OutputImageSize[0] += self.BorderSize_px * (XTileCounter + 1)
                OutputImageSize[1] += self.BorderSize_px * (YTileCounter + 1)
            OutputSliceImage = PIL.Image.new("RGBA", OutputImageSize, (0, 255, 0, 255))

            for x in range(XTileCounter):
                for y in range(YTileCounter):

                    try:
                        TileImage = PIL.Image.open(_DirectoryPath + _FileNames[ThisSliceNumber] + f"/{x}X_{y}Y.png")
                        
                        # Optionally Label The Images Based On Position
                        if (self.LabelImages):

                            Overlay = PIL.ImageDraw.Draw(TileImage)
                            Overlay.text((16, 16), f"X{x}, Y{y}, Slice {ThisSliceNumber}", fill=(255, 0, 0))

                        
                        position = [x * ReferenceImageSize[0],  y * ReferenceImageSize[1]]  # Corrected positions
                        if (self.AddBorders):
                                    position[0] += ((x + 1) * self.BorderSize_px)
                                    position[1] += ((y + 1) * self.BorderSize_px)

                        OutputSliceImage.paste(TileImage, position)
                        HasFoundImage = True
                        # break

                    except FileNotFoundError:
                        print(f"Failed To Find Image: '{x}X_{y}Y.png'")
                        # pass

                        # if (HasFoundImage):
                            # break
                    
                    # if (not HasFoundImage):
                    #     if (self.Verbose):
                    #         print(f"Error, could not find image for position {xposition}x, {yposition}y")
        
            # get slice number as a variable then use f string and i = i+1
            OutputImageFilename = f"{_OutputDir}/Slice{ThisSliceNumber}.png"
            OutputSliceImage.save(OutputImageFilename)
            if (self.MakeGif):
                SliceFilenames.append(OutputImageFilename)

            if (self.Verbose):
                print(f"     - Stitched Slice {ThisSliceNumber} ({XTileCounter}x{YTileCounter} images)")

        # Now, Create The Gif
        if (self.MakeGif):

            if (self.Verbose):
                print(f"    - Cresting Gif, This May Take A While")

            GifFilename:str = f"{_OutputDir}/Out.gif"
            with imageio.get_writer(GifFilename, mode='I', loop=0) as Writer:
                for Filename in SliceFilenames:
                    Image = imageio.v3.imread(Filename)
                    ImageNoAlpha = Image[:,:,:3]
                    Writer.append_data(ImageNoAlpha)


            if (self.Verbose):
                print(f"    - Created Gif For Simulation")



def StackStitcher(_InputDirectory:str, _OutputDirectory:str="OutDir", _AddBorders:bool=True, _LabelImages:bool=True, _BorderSize_px:int=8, _MakeGif:bool=True, _Verbose=True):

    # Ensure Paths Ends With /
    if not _InputDirectory.endswith("/"):
        _InputDirectory += "/"

    # Setup Slice Stitcher
    SS:SliceStitcher = SliceStitcher(_Verbose, _AddBorders, _BorderSize_px, _LabelImages, _MakeGif)

    # Reconstruct
    SlicesList = os.listdir(_InputDirectory)
    if (_Verbose):
        print(f" - Stitching Simulation")

        if (_Verbose):
            print(f"  - Stitching Now")
        SS.StitchSlice(_InputDirectory, _OutputDirectory, SlicesList)


