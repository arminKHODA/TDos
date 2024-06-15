import os
import time
from PIL import Image
from multiprocessing import Pool
from tqdm import tqdm

def format_time(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

def process_single_image(args):
    image_path, folder, chain, humandetection = args
    try:
        with Image.open(image_path) as img:
            img = img.convert("RGB")
            base_name = os.path.basename(image_path)
            new_name = os.path.splitext(base_name)[0] + ".jpg"
            img.save(os.path.join(folder, "jpg_result", new_name), "JPEG")
        return image_path, True
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return image_path, False

def process_image_batch(updated_image_list, folder, chain=False, humandetection=False, BATCH_SIZE=100):
    start_time = time.time()
    total_batches = (len(updated_image_list) + BATCH_SIZE - 1) // BATCH_SIZE

    for i in range(total_batches):
        batch_start_time = time.time()
        
        start_index = i * BATCH_SIZE
        end_index = min((i + 1) * BATCH_SIZE, len(updated_image_list))
        image_batch_paths = updated_image_list[start_index:end_index]
        print(f"Processing batch {i + 1}/{total_batches} with {len(image_batch_paths)} images...")

        with Pool(processes=os.cpu_count()) as pool:
            results = list(tqdm(pool.imap_unordered(process_single_image, [(image_path, folder, chain, humandetection) for image_path in image_batch_paths]), total=len(image_batch_paths), desc="Processing images in batch", leave=False))

        batch_end_time = time.time()
        batch_elapsed_time = batch_end_time - batch_start_time
        formatted_batch_time = format_time(batch_elapsed_time)
        print(f"Batch {i + 1} processed in {formatted_batch_time}")

    end_time = time.time()
    total_elapsed_time = end_time - start_time
    formatted_total_time = format_time(total_elapsed_time)
    print(f"All batches processed in {formatted_total_time}")
    print("All batches processed.")

def main():
    folder_path = input("Enter the path to the folder containing images: ")

    if not os.path.exists(folder_path):
        print("Invalid folder path.")
        return

    image_extensions = (".png", ".PNG", ".jpeg", ".JPEG", ".jpg", ".JPG", ".bmp", ".BMP", ".gif", ".GIF", ".tiff", ".TIFF")
    updated_image_list = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(image_extensions)]

    if not updated_image_list:
        print("No images found in the folder.")
        return

    jpg_result_folder = os.path.join(folder_path, "jpg_result")
    original_image_folder = os.path.join(folder_path, "original_image")

    os.makedirs(jpg_result_folder, exist_ok=True)
    os.makedirs(original_image_folder, exist_ok=True)

    process_image_batch(updated_image_list, folder_path, BATCH_SIZE=10)

    for image_path in updated_image_list:
        base_name = os.path.basename(image_path)
        os.rename(image_path, os.path.join(original_image_folder, base_name))

if __name__ == "__main__":
    main()
