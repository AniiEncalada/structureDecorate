/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package unl.cis.swem.creationalpatterns.view;


import unl.cis.swem.creationalpatterns.factorymethod.AdministrativePersonalFactory;
import unl.cis.swem.creationalpatterns.factorymethod.PersonFactoryMethod;
//import unl.cis.swem.creationalpatterns.factorymethod.StudentFactory;
//import unl.cis.swem.creationalpatterns.factorymethod.TeacherFactory;


import unl.cis.swem.creationalpatterns.domain.*;

/**
 *
 * @author wduck
 */
public class FactoryMethodMain {

    public static void main(String[] args) {
       
        System.out.println(" ===============================");
        
        System.out.println(" ========== PATRON FACTORY METHOD =====");
        
        PersonFactoryMethod personFactory;
        //personFactory = new TeacherFactory();
        //personFactory = new StudentFactory();
        personFactory = new AdministrativePersonalFactory();
        
        Person object = personFactory.create();
        System.out.println(object.toString());
        System.out.println();
        System.out.println(object.fullName());
        //object.task();

        System.out.println(" ===============================");
        
        System.out.println(" ========== PATRON SINGLETON =====");

        University objUniversidad1 = University.getUniversity("UNL", "La Argelia");
        objUniversidad1.presentar();
        System.out.println("objUniversidad1: " + objUniversidad1.toString());
        
        University objUniversidad2 = University.getUniversity("UTPL", "San Cayetano");
        objUniversidad2.presentar();
        System.out.println("objUniversidad2: " + objUniversidad2.toString());
        System.out.println("objUniversidad1: " + objUniversidad1.toString());

    }




}
