int romanToInt(char * s)
{
    int i = 0, result = 0, previous_value = 0, value = 0;

    while (s[i] != '\0') {
        char letter = s[i];
        switch (letter) {
            case 'I':
                value = 1;
                break;
            case 'V':
                value = 5;
                break;
            case 'X':
                value = 10;
                break;
            case 'L':
                value = 50;
                break;
            case 'C':
                value = 100;
                break;
            case 'D':
                value = 500;
                break;
            case 'M':
                value = 1000;
                break;
        }
        result += value;
        if (value > previous_value) {
            result -= 2 * previous_value;
        }
        previous_value = value;
        i++;
    }
    return result;
}
