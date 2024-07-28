from faker import Faker
from random import randint


def get_a_list_of_sizes(n):
    """
    Create a list of numbers that 
    will be used when creating a photo

    Args:
        n (int): количество чисел для формирование стороны фото

    Returns:
        _type_: list
    """

    base = []
    for i in range(n):
        base.append(randint(400, 800))
    return base


def create_photo_storage(width=get_a_list_of_sizes(30), height=get_a_list_of_sizes(20)):
    """

    The function returns a sorted list of high-quality 
    photos from unusable ones. We use the faker module 
    to generate URLs for photos. If the function receives
    objects of different lengths, then using the zip 
    function it will filter out unnecessary values

    Args:
        width (list or tuple): ширина фото. Defaults to get_a_list_of_sizes(30).
        height (list or tuple): высота фото. Defaults to get_a_list_of_sizes(20).

    Returns:
        _type_: list
    """
    try:
        zip_archive = zip(width, height)

        address_storage = []
        for photo_parameters in zip_archive:
            faker = Faker()
            create_image = faker.image_url(
                width=photo_parameters[0], height=photo_parameters[1])
            address_storage.append(create_image)

        filter_for_working_photosaddress_storage = list(
            filter(lambda photo: ".photos/" in photo, address_storage))

        return filter_for_working_photosaddress_storage
    except TypeError:
        return "Arguments error, please enter two iterable object arguments(list,tuple)"
