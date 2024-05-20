#include <iostream>

// ovenTime returns the amount in minutes that the lasagna should stay in the
// oven.
int ovenTime() {
    // TODO: Return the correct time.
    return 40;
}

/* remainingOvenTime returns the remaining
   minutes based on the actual minutes already in the oven.
*/
int remainingOvenTime(int actualMinutesInOven) {
    // TODO: Calculate and return the remaining in the oven based on the time
    // the lasagna has already been there.
    int totalTime= ovenTime();
    return totalTime-actualMinutesInOven;
}

/* preparationTime returns an estimate of the preparation time based on the
   number of layers and the necessary time per layer.
*/
int preparationTime(int numberOfLayers) {
    // TODO: Calculate and return the preparation time with the
    // `numberOfLayers`.
    return numberOfLayers*2;
}
// elapsedTime calculates the total time spent to create and bake the lasagna so
// far.
int elapsedTime(int numberOfLayers, int actualMinutesInOven) {
    // Calculate the preparation time using the `preparationTime` function
    int prepTime = preparationTime(numberOfLayers);
    
    // Return the total time spent so far, which is the sum of preparation time and actual minutes in the oven
    return prepTime + actualMinutesInOven;
}



int main() {
    int tiempoCoccion = ovenTime();
    // Print the cooking time of the lasagna
    std::cout << "Tiempo de cocción de la lasaña: " << tiempoCoccion << " minutos" << std::endl;

    // Call remainingOvenTime() function with the obtained cooking time
    int tiempoRestante = remainingOvenTime(10);
    // Print the remaining time in the oven
    std::cout << "Tiempo restante en el horno: " << tiempoRestante << " minutos" << std::endl;

    int time = preparationTime(4);
    // Imprime los resultados
    std::cout << "Preparation time for " <<  " layers: " << time << " minutes" << std::endl;
   
    return 0;
}