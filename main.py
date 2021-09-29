def cal_kernel (kernel, input_image, edge_mode):
    if (edge_mode == 'O'):
        pass
    
    elif (edge_mode == 'S'):
        input_image.insert(0,[0]*len(input_image[0]))
        input_image.append([0]*len(input_image[0]))
        for k in range(len(input_image)):
            input_image[k].insert(0,0)
            input_image[k].append(0)
 
    elif (edge_mode == 'P'):
        black = 0
        white = 255
        
        input_image.insert(0,[black]*len(input_image[0]))
        input_image.append([black]*len(input_image[0]))
        for k in range(len(input_image)):
            input_image[k].insert(0,white)
            input_image[k].append(white)            
             
    elif (edge_mode == 'R'):
        input_image.insert(0,input_image[0]+[])
        input_image.append(input_image[-1]+[])
        for k in range(len(input_image)):
            input_image[k].insert(0,input_image[k][0])
            input_image[k].append(input_image[k][-1])
    
    elif (edge_mode == 'W'):
        input_image.insert(0,input_image[-1]+[])
        input_image.append(input_image[1]+[])
        for k in range(len(input_image)):
            input_image[k].insert(0,input_image[k][-1])
            input_image[k].append(input_image[k][1])
        
        
    N = len(input_image)
    M = len(input_image[0])
    result = [] 
    # Compute convolution between intensity and kernels
    for y in range(1, N - 1):
        row_result = []
        for x in range(1, M - 1):
            conv_val = 0
            for a in range(len(kernel)):
                for b in range(len(kernel[a])):
                    total = (kernel[a][b]*input_image[y-1+a][x-1+b])
					conv_val+=total
            row_result.append(conv_val)
        result.append(row_result)
            
    return result