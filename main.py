import face_recognition
import glob, os
import time
from PIL import Image, ImageDraw
from openpyxl import Workbook
from logger import logger
import multiprocessing
from tqdm import tqdm


def parallel_run(file):
    face_count = find_face(file)
    return [file, face_count]

def main():
    start_time = time.time()
    logger.info('Begin')

    wb = Workbook()
    ws = wb.active
    ws['A1'] = '檔案名'
    ws['B1'] = '人臉數目'
    ws['C1'] = '有無眨眼'
    files = glob.glob("P:\\數碼相機\\2017-09-30\\*.jpg")
    # div = round(len(files) / 10)
    div = round(len(files) / 100)

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    pbar = tqdm(total=len(files))
    for i, (file, face_count) in tqdm(enumerate(pool.imap(parallel_run, files))):
        ws.append([file, face_count])
        pbar.update()

    # results = pool.map(parallel_run, enumerate(files))
    pool.close()
    pool.join()
    # for file, face_count in results:
    #     ws.append([file, face_count])

    wb.save("sample.xlsx")

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info('End')
    logger.info('Elapsed %s', elapsed_time)


def find_face(filename):
    image = face_recognition.load_image_file(filename)
    face_locations = face_recognition.face_locations(image)
    # face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")

    # face_encodings = face_recognition.face_encodings(image, face_locations)
    # pil_image = Image.fromarray(image)
    # draw = ImageDraw.Draw(pil_image)
    # for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    #     # See if the face is a match for the known face(s)
    #     #matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    #     name = "Unknown"
    #     # If a match was found in known_face_encodings, just use the first one.
    #     # if True in matches:
    #     #     first_match_index = matches.index(True)
    #     #     name = known_face_names[first_match_index]

    #     # Draw a box around the face using the Pillow module
    #     draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    #     # Draw a label with a name below the face
    #     #text_width, text_height = draw.textsize(name)
    #     draw.rectangle(((left + 10, top), (left, bottom)), fill=(255, 0, 0), outline=(255, 0, 0))
    #     draw.rectangle(((left, top + 10), (right, top)), fill=(255, 0, 0), outline=(255, 0, 0))
    #     draw.rectangle(((left, bottom - 10), (right, bottom)), fill=(255, 0, 0), outline=(255, 0, 0))
    #     draw.rectangle(((right - 10, top), (right, bottom)), fill=(255, 0, 0), outline=(255, 0, 0))
    #     #draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

    # # Remove the drawing library from memory as per the Pillow docs
    # del draw
    # del pil_image

    return len(face_locations)

    # Display the resulting image
    #pil_image.show()
    # new_width  = 800
    # new_height = new_width * pil_image.size[0] / pil_image.size[1]
    # pil_image.thumbnail((new_width, new_height), Image.ANTIALIAS)
    # pil_image.save("r:\\MMA_4097ok.JPG", 'JPEG', quality=50)


main = main

if __name__ == "__main__":
    main()