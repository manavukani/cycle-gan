# Season Translation Using CycleGAN

## Overview

Generative Adversarial Networks (GANs) are machine learning frameworks designed to generate realistic images. CycleGAN, in particular, enables image-to-image translation without the need for paired datasets. This project specifically focuses on translating seasonal images, such as from summer to winter and vice versa, using CycleGAN.

## Dataset

- **Source:** UC Berkeley
- **Images:** 1279 photos of Yosemite in summer and winter
- **Type:** Unpaired
- **Format:** JPEG
- **Size:** 256 x 256 pixels
- **Classes:** 2 (Summer, Winter)
- **Split:** 80% training, 20% testing

## Architecture

The CycleGAN architecture consists of:
- Two Generators (G and F): For translating images from summer to winter and winter to summer.
- Two Discriminators (D_X and D_Y): For evaluating the authenticity of the generated images.

### Key Components:
- **Generators (G and F):** Transform images between domains.
- **Discriminators (D_X and D_Y):** Distinguish real images from generated ones.
- **Cycle Consistency Loss:** Ensures that an image can be translated to the target domain and back to the original domain.

## Usage

To run the Streamlit application:
```bash
streamlit run app.py
```

## Files and Folders

- **checkpoints/**: Stores model checkpoints.
- **data/**: Contains dataset-related files.
- **models/**: Includes model architecture and utilities.
- **options/**: Configuration files for training and testing.
- **summer/**: Contains test summer images.
- **summer2winter_yosemite/**: Contains training data for summer to winter translation.
- **util/**: Utility scripts.
- **winter/**: Contains test winter images.
- **app.py**: Streamlit application for interactive UI.
- **style_converter.py**: Core script for image style conversion using CycleGAN.
- **video.py**: work in progress!

## Results

The results of the season translation demonstrate effective and realistic transformations between summer and winter scenes. Both qualitative and quantitative evaluations (SSIM, PSNR) show high performance and user satisfaction.

### Input
![input](https://github.com/user-attachments/assets/92e8031b-9184-4056-84c7-29b74302d27b)
### Output
![output](https://github.com/user-attachments/assets/9b34888e-464c-4c68-9ad8-09df66784900)


## New Features
- Implement the video translation functionality

## References

- Goodfellow, I., et al. (2014). Generative Adversarial Nets. Advances in Neural Information Processing Systems.
- Isola, P., et al. (2017). Image-to-Image Translation with Conditional Adversarial Networks. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition.
- Zhu, J. Y., et al. (2017). Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks. Proceedings of the IEEE International Conference on Computer Vision.

---

This project was created as a part of the Machine Learning (Lab) course. <be>
##### Contributors

- Manav Ukani (20BCP167)
- Jenis Gundaraniya (20BCP157)
