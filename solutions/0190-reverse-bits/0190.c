#include <stdint.h>

uint32_t reverseBits(uint32_t n) {
    uint32_t ret = 0, power = 31;
    
    while (n != 0) {
      ret += (n & 1) << power;
      n >>= 1;
      power -= 1;
    }
    return ret;
}
