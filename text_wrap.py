import textwrap

def wrap(string, max_width):
    wrapper_width = textwrap.TextWrapper(max_width)
    output_paragraph = wrapper_width.wrap(string)
    
    return "\n".join(output_paragraph)
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)