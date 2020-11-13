#include <stdint.h>

uint32_t reverseBits(uint32_t n) {
    uint32_t ret = 0, power = 31;
    
    while (n) {
      ret += (n & 1) << power;
      n >>= 1;
      power--;
    }
    return ret;
}
