package unl.cis.swem.creationalpatterns.view;

import unl.cis.swem.creationalpatterns.decorator.PersonExtraHours;
import unl.cis.swem.creationalpatterns.decorator.PersonFeature;
import unl.cis.swem.creationalpatterns.domain.AdministrativePersonal;
import unl.cis.swem.creationalpatterns.domain.Person;
import unl.cis.swem.creationalpatterns.domain.SocialEconomicLevel;
import unl.cis.swem.creationalpatterns.domain.Student;
import unl.cis.swem.creationalpatterns.domain.Task;
import unl.cis.swem.creationalpatterns.domain.Teacher;

public class Index {

    public static void main(String[] args) {

       Task person = new Person("Juan", "Peréz", "12345");
       person.tarea();

       person= new PersonFeature(person);
        person.tarea();
        System.out.println("-------------------------------------------------");
        Task student = new Student("Karina", "Peréz", "12345", SocialEconomicLevel.LOW);

        student.tarea();
        student = new PersonFeature(student);
        student.tarea();
        System.out.println("-------------------------------------------------");
        Task teacher = new Teacher("Carlos", "Maldonado", "2345", "PhD");
        teacher.tarea();
        teacher = new PersonExtraHours(teacher);
        teacher.tarea();
        System.out.println("-------------------------------------------------");
        Task administrativePersonal = new AdministrativePersonal("Jane", "Jons", "1234", "Manager");
        administrativePersonal.tarea();
        administrativePersonal = new PersonExtraHours(administrativePersonal);
        administrativePersonal.tarea();
    }
    
}
