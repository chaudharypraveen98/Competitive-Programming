import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// Base class representing a generic flower
class Flower {

    // Method to return the name of the flower
    String whatsYourName(){
        return "I have many names and types.";
    }

}

// Subclass representing a Jasmine flower
class Jasmine extends Flower{

    // Override the method to return the specific name "Jasmine"
    @Override
    String whatsYourName(){
        return "Jasmine";
    }

}

// Subclass representing a Lily flower
class Lily extends Flower{

    // Override the method to return the specific name "Lily"
    @Override
    String whatsYourName(){
        return "Lily";
    }

}

// Base class representing a region
class Region {

    // Method to return the national flower of the region
    Flower yourNationalFlower(){
        return new Flower();  // Default implementation returns a generic flower
    }

}

// Subclass representing the West Bengal region
class WestBengal extends Region{

    // Override the method to return Jasmine as the national flower
    @Override
    Flower yourNationalFlower(){
        return new Jasmine();
    }

}

// Subclass representing the Andhra Pradesh region
class AndhraPradesh extends Region{

    // Override the method to return Lily as the national flower
    @Override
    Flower yourNationalFlower(){
        return new Lily();
    }

}


public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String s = reader.readLine().trim();
        Region region = null;
        switch (s) {
            case "WestBengal":
                region = new WestBengal();
                break;
            case "AndhraPradesh":
                region = new AndhraPradesh();
                break;
        }
        Flower flower = region.yourNationalFlower();
        System.out.println(flower.whatsYourName());
    }
}