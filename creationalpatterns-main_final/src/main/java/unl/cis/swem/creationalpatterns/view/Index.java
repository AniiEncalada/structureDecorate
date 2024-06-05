package unl.cis.swem.creationalpatterns.view;

import unl.cis.swem.creationalpatterns.decorator.*;
import unl.cis.swem.creationalpatterns.domain.*;

public class Index {

    public static void main(String[] args) {

       Task person = new Person("Juan", "Peréz", "12345");
       person.tarea();

       person= new PersonFeature(person);
        person.tarea();
        System.out.println("-------------------------------------------------\n");
        Task student = new Student("Karina", "Peréz", "12345", SocialEconomicLevel.LOW);

        student.tarea();
        student = new PersonBonus(student);
        student.tarea();
        System.out.println("-------------------------------------------------\n");
        Task teacher = new Teacher("Carlos", "Maldonado", "2345", "PhD");
        teacher.tarea();
        teacher = new PersonExtraHours(teacher);
        teacher.tarea();
        System.out.println("-------------------------------------------------\n");
        Task administrativePersonal = new AdministrativePersonal("Jane", "Jons", "1234", "Manager");
        administrativePersonal.tarea();
        administrativePersonal = new PersonExtraHoursAndBonus(administrativePersonal);
        administrativePersonal.tarea();
    }
    
}
