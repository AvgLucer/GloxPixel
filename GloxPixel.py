# Glox Pixel is a Python CLI Based Application/Terminal Application that lets u optimize , enhance , filter , convert your images | Offline , Secure 
from PIL import Image, ImageEnhance , ImageFilter
import time as t


#Enhancer Function

def img_enhance():
    ext2 = input("Select Image Extension: 1. JPEG, 2. PNG, 3. WebP 4. JPG: ")
    if ext2 == "1":
        ext = ".jpeg"
    elif ext2 == "2":
        ext = ".png"
    elif ext2 == "3":
        ext = ".webp"
    elif ext2 == "4":
        ext = ".jpg"
    else:
        print("Invalid Extension Choice")
        exit()

    name = input("Enter name of the Image: ")

    preset = input("Select Preset:  1.Noir , 2. Radiance , 3.Chromatic , 4.Clarity , 5. Aqua , 6. Dusk , 7. Vintage  , 8. Forest , 9. Cinematic , 10. Amethyst : ")
    img1 = name + ext

    if preset == "1":
        img = Image.open(img1)
        img = ImageEnhance.Sharpness(img).enhance(1.15)
        img = ImageEnhance.Color(img).enhance(1.15)
        img = ImageEnhance.Brightness(img).enhance(0.75)
        img = ImageEnhance.Contrast(img).enhance(1.125)
        overlay = Image.new("RGB", img.size, (25, 20, 35))
        img = Image.blend(img.convert("RGB"), overlay, 0.095)
        img.save("Noir_" + img1)
        
    elif preset == "2":
        img = Image.open(img1)
        img = ImageEnhance.Sharpness(img).enhance(1.15)
        img = ImageEnhance.Color(img).enhance(1.15)
        img = ImageEnhance.Brightness(img).enhance(1.2)
        img = ImageEnhance.Contrast(img).enhance(1.125)
        overlay = Image.new("RGB", img.size, (255, 220, 120))
        img = Image.blend(img.convert("RGB"), overlay, 0.095)
        img.save("Radiance_" + img1)
        
    elif preset == "3":
        img = Image.open(img1)
        img = ImageEnhance.Sharpness(img).enhance(1.305)
        img = ImageEnhance.Color(img).enhance(1.105)
        img = ImageEnhance.Brightness(img).enhance(1.0)
        img = ImageEnhance.Contrast(img).enhance(1.105)
        overlay = Image.new("RGB", img.size, (180, 180, 180))
        img = Image.blend(img.convert("RGB"), overlay, 0.15)
        img.save("Chromatic_" + img1)
        
    elif preset == "4":
        img = Image.open(img1)
        img = ImageEnhance.Sharpness(img).enhance(1.35)
        img = ImageEnhance.Color(img).enhance(1.15)
        img = ImageEnhance.Brightness(img).enhance(1.1)
        img = ImageEnhance.Contrast(img).enhance(1.2)
        img.save("Clarity_" + img1)    
    elif preset == "5":
        img = Image.open(img1)
        img = ImageEnhance.Sharpness(img).enhance(1.15)
        img = ImageEnhance.Color(img).enhance(1.15)
        img = ImageEnhance.Brightness(img).enhance(1.05)
        img = ImageEnhance.Contrast(img).enhance(1.125)
        overlay = Image.new("RGB", img.size, (20, 70, 150))
        img = Image.blend(img.convert("RGB"), overlay, 0.25)
        img.save("Aqua_" + img1)
    elif preset == "6":
        img = Image.open(img1)
        img = ImageEnhance.Sharpness(img).enhance(1.2)
        img = ImageEnhance.Color(img).enhance(1.05)
        img = ImageEnhance.Brightness(img).enhance(0.715)
        img = ImageEnhance.Contrast(img).enhance(1.115)
        overlay = Image.new("RGB", img.size, (100, 85, 55))
        img = Image.blend(img.convert("RGB"), overlay, 0.15)
        img.save("Dusk_" + img1)
    elif preset == "7":
        img = Image.open(img1)
        img = ImageEnhance.Sharpness(img).enhance(1.05)
        img = ImageEnhance.Color(img).enhance(0.995)
        img = ImageEnhance.Brightness(img).enhance(0.995)
        img = ImageEnhance.Contrast(img).enhance(1.005)
        overlay = Image.new("RGB", img.size, (175,170,115))
        img = Image.blend(img.convert("RGB"), overlay, 0.25)
        img.save("Vintage_" + img1)
    elif preset == "8":
        img = Image.open(img1)
        img = ImageEnhance.Sharpness(img).enhance(1.075)
        img = ImageEnhance.Color(img).enhance(1.05)
        img = ImageEnhance.Brightness(img).enhance(0.995)
        img = ImageEnhance.Contrast(img).enhance(0.9995)
        overlay = Image.new("RGB", img.size, (85 , 195 , 125))
        img = Image.blend(img.convert("RGB"), overlay, 0.195)
        img.save("Forest_" + img1)
    elif preset == "9":
        img = Image.open(img1)
        img = ImageEnhance.Sharpness(img).enhance(1.25)
        img = ImageEnhance.Color(img).enhance(1.25)
        img = ImageEnhance.Brightness(img).enhance(1.055)
        img = ImageEnhance.Contrast(img).enhance(0.995)
        overlay = Image.new("RGB", img.size, (25,35,15))
        img = Image.blend(img.convert("RGB"), overlay, 0.25)
        img.save("Cinematic_" + img1)
    elif preset == "10":
        img = Image.open(img1)
        img = ImageEnhance.Sharpness(img).enhance(1.15)
        img = ImageEnhance.Color(img).enhance(1.15)
        img = ImageEnhance.Brightness(img).enhance(1.1)
        img = ImageEnhance.Contrast(img).enhance(1.05)
        overlay = Image.new("RGB", img.size, (135,80,145))
        img = Image.blend(img.convert("RGB"), overlay, 0.25)
        img.save("Amethyst_" + img1)

#Filtering Function

def img_filter():
    exte = input("Choose File Extension: 1. jpeg 2. png 3. webp : ")
    if exte == "1":
        opens = input("Enter File name : ")
        x = opens + ".jpg"
        img = Image.open(opens + ".jpg")
        
    elif exte == "2":
        opens = input("Enter File name")
        x = opens + ".png"
        img = Image.open(opens+ ".png")
    elif exte == "3":
        opens = input("Enter File name")
        x = opens + ".webp"
        img = Image.open(opens + ".webp")
    else:
        print("Wrong Input! , Please Restart.")
        exit()
        

    choose = input("Enter Choice : 1. Sharpen 2. Smoothen 3. FIND_Edge 4. Detail : ")
    if choose == "1":
        final = img.filter(ImageFilter.SHARPEN)
        final.save("sharp_" + x)
    elif choose == "2":
        final = img.filter(ImageFilter.SMOOTH)
        final.save("smooth_" + x)
    elif choose == "3":
        final = img.filter(ImageFilter.FIND_EDGES)
        final.save("find_edges_" + x)
    elif choose == "4":
        final = img.filter(ImageFilter.DETAIL)
        final.save("detail_" + x)
    else:
        print("Wrong Input! , Please Restart.")
        exit()



#Optimizing Function


def img_optimize():
        try:
            print("~~~~~~~~~Image Optimizer~~~~~~~~~")
            ext = int(input("Select Type of Image : 1. JPEG 2. PNG 3. webp :"))
            name = input("Enter name of the Image : ")
            if ext == 1:
                final = name + ".jpeg"
            elif ext == 2:
                final = name + ".png"

            elif ext == 3:
                final = name + ".webp"
            else:
                print("Invalid Digit , Restart Please")
                
            with Image.open(final) as opens:
                opt = int(input("Select Level of Optimization :" \
                " 1. Level 1 [High Quality , Less Optimization]" \
                " 2. Level 2 [Medium Quality , Medium Optimization]" \
                " 3. Level 3 [Low Quality , High Optimization]"))
                if ext == 1 or ext == 3:
                    if opt == 1:
                        opens.save(f"OptL1_{final}" , quality = 85 , optimize = True)
                        print("Sucessfully Optimized!")
                    elif opt == 2:
                        opens.save(f"OptL2_{final}" , quality = 75 , optimize = True)
                        print("Sucessfully Optimized!")

                    elif opt == 3:
                        opens.save(f"OptL3_{final}" , quality = 65 , optimize = True)
                        print("Sucessfully Optimized!")
                    else : 
                        print("Invalid Optimization Level , Please Restart!")
                        
                elif ext == 2:
                    if opt == 1:
                        opens.save(f"OptL1_{final}" , compress_level = 3 , optimize = True)
                        print("Sucessfully Optimized!")
                    elif opt == 2:
                        opens.save(f"OptL2_{final}" , compress_level = 6 , optimize = True)
                        print("Sucessfully Optimized!")

                    elif opt == 3:
                        opens.save(f"OptL3_{final}" , compress_level = 9 , optimize = True)
                        print("Sucessfully Optimized!")
                    else : 
                        print("Invalid Optimization Level , Please Restart!")
                        
                else:
                    print("Invalid Input , Please Restart ")
        except FileNotFoundError as e :
            print("Error Occured :" , e)
        except ValueError:
            print("Please enter a valid number!")


#Image Format Converter

def convert():
    input_file = input("Input file[With Extension]: ")
    output_file = input("Output file[With Extension]: ")

    img = Image.open(input_file)
    img.save(output_file)

    print("✅ Conversion successful!")




#Menu

while True:
    print("~~~~~~~~~~~GLOX PIXEL~~~~~~~~~~~")
    option = int(input("~~~Select the Option Below~~~\n" \
    "1. Image Enhancer\n" \
    "2. Image Filtering\n" \
    "3. Image Format Conversion\n" \
    "4. Image Optimizer\n"
    "->"))

    if option == 1:
        img_enhance()
        print("Enhanced Sucessfully!")
        t.sleep(3)
    elif option ==2:
        img_filter()
        print("Filtered Sucessfully!")
        t.sleep(3)
    elif option ==3:
        convert()
        print("Converted Sucessfully!")
        t.sleep(3)
    elif option ==4:
        img_optimize()
        print("Optimized Sucessfully!")
        t.sleep(3)
    else:
        print("Invalid Option , Please Restart")
        break

#Credits : AvgLucer | Gaurav W