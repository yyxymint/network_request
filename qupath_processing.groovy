import qupath.lib.regions.RegionRequest
import qupath.lib.images.writers.ImageWriterTools

// Set your desired downsampling factor
double downsampleFactor = 8.0

// Output file path
def outputPath = "C:/Users/user/Desktop/smc_testing/dsf.png"

// Get image server
def server = getCurrentServer()

// Request the full region at downsampled resolution
def request = RegionRequest.createInstance(
    server.getPath(), 
    downsampleFactor, 
    0, 
    0, 
    server.getWidth(), 
    server.getHeight()
)

// Read the downsampled BufferedImage
def img = server.readBufferedImage(request)

// Write the BufferedImage directly to PNG
ImageWriterTools.writeImage(img, outputPath)

println "Export completed successfully: " + outputPath
