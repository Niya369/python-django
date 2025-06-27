# from django import template

# register = template.Library()

# @register.filter(name='chunks')
# def chunks(list_data,chunk_size):
#     chunk=[]
#     i=0
#     for data in list_data:
#         chunk.append(data)
#         i=i+1
#         if i==chunk_size:
#             yield chunk
#             i=0
#             chunk=[]
#     yield chunk
    


# register = template.Library()

# @register.filter
# def chunks(value, size):
#     """Breaks a list into chunks of given size."""
#     if not value:
#         return []

#     try:
#         size = int(size)

#         def chunk_generator():
#             for i in range(0, len(value), size):
#                 yield value[i:i + size]

#         return chunk_generator()
#     except (ValueError, TypeError):
#         return []

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


# register = template.Library()  #  This line MUST come before using @register.filter

# @register.filter(name='chunks')
# def chunks(list_data, chunk_size):
#     if not list_data:
#         return []

#     try:
#         chunk_size = int(chunk_size)
#     except (ValueError, TypeError):
#         return [list_data]

#     result = []
#     chunk = []

#     for i, data in enumerate(list_data, 1):
#         chunk.append(data)
#         if i % chunk_size == 0:
#             result.append(chunk)
#             chunk = []

#     if chunk:
#         result.append(chunk)

#     return result
