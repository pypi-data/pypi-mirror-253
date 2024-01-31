from typing import TypeVar

T = TypeVar('T')

def split_into_batches(initial_list: list[T], batch_size: int) -> list[list[T]]:
    """ Splits a list into multiple batches.
    
    Args:
        initial_list (List[T]): The list to split.
        batch_size (int): The size of each batch.
    
    Returns:
        List[List[T]]: A list of batches.
    """
    return [initial_list[i:i + batch_size] for i in range(0, len(initial_list), batch_size)]