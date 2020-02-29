#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <getopt.h>


float arc_length(float,float);
double get_radians(float);
float get_area(float);
void print_usage(void);
float area_of_square_from_arc(float, float);
float area_of_square(float);
float line_to_square_side(float);

int main(int argc, char** argv) {
    int option;
    float angle, radius ;
    if (argc != 5){
        print_usage();
    }
    while ((option = getopt(argc, argv,"a:r:")) !=-1){
        switch (option){
            case 'a' : 
                angle = atof(optarg);
                break;
            case 'r' :
                radius = atof(optarg);
                break;
            default :
                print_usage();
        }
    }
    // printf("got radius = %.2f, angle = %.2f degrees",radius,angle);
    float area = area_of_square_from_arc(angle, radius);
    printf("Area of square formed from an arc of radius %.2f and angle %.2f degrees is %.3f", radius,angle,area );
    return 0;
}


float area_of_square_from_arc(float arc_angle, float arc_radius){
    float arc_len = arc_length(arc_angle, arc_radius);
    float side_len = line_to_square_side(arc_len);
    return area_of_square(side_len);
}

float area_of_square(float side_length){
    return side_length*side_length;
}

float line_to_square_side(float length){
    float square_side_length = length/4;
    return square_side_length;
}

float arc_length(float angle, float radius){
    double radians = get_radians(angle);
    return radians*radius;
}

double get_radians(float degrees){
    return (M_PI/180) * degrees;
}

void print_usage(){
    printf("Usage: a.exe -r <radius> -a <angle in degrees>\n");
    exit(2);
}