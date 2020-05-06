# Eye Blink Detection

### Source Encoding Model

  - At present, we are using 10 bits to encode the data bit. Thus, we can think of this as a Repetition(10, 1) scheme. 
  - We also are using all 16 combinations of the 4 bit input data sequence (40 bit encoded sequence). Thus, the input data has a *minimum hamming distance* of **1**
  - If we combine this fact along with our encoding scheme, the *effective minimum hamming distance* is **10**
        
    $$\lfloor \frac{10}{2} \rfloor = 4$$
  - Thus, this encoding scheme can correct upto 4 bits. 
  - Similarly, if we increase the minimum hamming distance of the input data to **2** by considering only 4 out of the 16 4 bit schemes, the *minimum effective hamming distance* is now **20**, and this can correct upto **9** bits.

### Theoretical Evaluation 

  - The probability of error for an encoding scheme can be theoretically calculated with the help of the number of bits that can be corrected. 

$$P_{out}(n, p)=\sum_{j=n/2}^{n} {\binom{n}{j}p^j(1-p)^{n-j}}$$

![img1](imgs/p_error.jpg)
*Input vs Output probability of error*
![img2](imgs/log_plot_p_error.jpg)
*Log plot for the same*

        
