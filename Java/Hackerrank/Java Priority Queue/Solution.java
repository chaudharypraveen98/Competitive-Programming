import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Comparator;
import java.util.PriorityQueue;

// Class representing a Student with ID, name, and CGPA


class Student {
    private final int id;
    private final String name;
    private final double cgpa;

    public Student(int id, String name, double cgpa) {
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }

    public int getID() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getCGPA() {
        return cgpa;
    }
}

// Class responsible for managing student priorities and processing events


class Priorities {

    // PriorityQueue to hold students, ordered by CGPA (descending), then name (lexicographically), then ID


    private final PriorityQueue<Student> queue = new PriorityQueue<>(
            Comparator.comparing(Student::getCGPA).reversed()           // First compare by CGPA in descending order
                    .thenComparing(Student::getName)                    // Then compare by name lexicographically
                    .thenComparing(Student::getID));                     // Finally compare by ID

    // Method to process events and return the remaining students in priority order

    public List<Student> getStudents(List<String> events) {
        // Loop through each event
        events.forEach((event) -> {
            if (event.equals("SERVED")) {
                // If the event is "SERVED", remove the student at the top of the queue
                queue.poll();
            } else {
                // Otherwise, extract student details from the "ENTER" event
                String[] details = event.split(" ");

                // Add the new student to the queue
                queue.add(new Student(Integer.parseInt(details[3]), details[1], Double.parseDouble(details[2])));
            }
        });
        // Prepare a list to store the remaining students in the correct order
        List<Student> students = new ArrayList<>();
        while (!queue.isEmpty()) {
            students.add(queue.poll());  // Remove students from the queue and add to the list
        }

        return students;         // Return the list of students
    }
}

public class Solution {
    private final static Scanner scan = new Scanner(System.in);
    private final static Priorities priorities = new Priorities();

    public static void main(String[] args) {
        int totalEvents = Integer.parseInt(scan.nextLine());
        List<String> events = new ArrayList<>();

        while (totalEvents-- != 0) {
            String event = scan.nextLine();
            events.add(event);
        }

        List<Student> students = priorities.getStudents(events);

        if (students.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Student st: students) {
                System.out.println(st.getName());
            }
        }
    }
}