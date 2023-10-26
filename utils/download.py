import requests
from tqdm import tqdm

url = 'https://ia804701.us.archive.org/15/items/tiny-10_202301/tiny10%202303%20x86.iso'
filename = 'tiny10 2303 x86.iso'

# Send a GET request to the URL
response = requests.get(url, stream=True)

# Get the file size from the response headers
file_size = int(response.headers.get('Content-Length', 0))

# Create a progress bar with the total file size
progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)

# Open a file for writing
with open(filename, 'wb') as f:
    # Iterate over the response content in chunks
    for chunk in response.iter_content(chunk_size=1024):
        # Write the chunk to the file
        f.write(chunk)
        
        # Update the progress bar with the number of bytes written
        progress_bar.update(len(chunk))

# Close the progress bar
progress_bar.close()

print('File downloaded successfully')
