from options.test_options import TestOptions
from util import util 
from models import create_model

import torchvision.transforms as transforms
from PIL import Image

opt = TestOptions().parse() 

def stylise(img,style="winter2summer"):
    opt.name= style
    opt.gpu_ids=[]
    opt.model= "test"
    opt.no_dropout = True   
    # opt.num_threads = 0   
    opt.batch_size = 1    
    opt.serial_batches = True  
    opt.no_flip = True   
    opt.display_id = -1  

    transform = transforms.Compose([
        transforms.Resize((1024,1024)),
        transforms.ToTensor(),
    ])
    
    img_tensor = transform(img).unsqueeze(0)   
    
    dataset=[
        {"A":img_tensor,
         'A_paths': ['seasons.jpg']
        }
    ]

    
    model = create_model(opt)      
    model.setup(opt)              

    losses = model.get_current_losses()
    for name, value in losses.items():
        print(f'{name}: {value}')
    for i, data in enumerate(dataset):
        if i >= opt.num_test:  
            break

        model.set_input(data)  
        model.test()           
        visuals = model.get_current_visuals()  
        loss = model.get_current_losses()
        # for key, value in loss.items():
        #     print(key, value)
        print(len(loss))
        for label, im_data in visuals.items():
            im = util.tensor2im(im_data)
            image_pil = Image.fromarray(im)
            if label=="fake":
                print("Done")
                return image_pil
# style="summer2winter"
# style="winter2summer"
# key_word=style[:6]
# p_img = "test"+key_word+"3.jpg"
# img = Image.open(key_word+"/"+p_img)
# final=stylise(img,style)
# final.show()
# path=key_word+"/conv_"+p_img
# im1 = final.save(str(path))