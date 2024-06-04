/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package unl.cis.swem.creationalpatterns.factorymethod;

import unl.cis.swem.creationalpatterns.domain.Person;
import unl.cis.swem.creationalpatterns.domain.SocialEconomicLevel;
import unl.cis.swem.creationalpatterns.domain.Student;

/**
 *
 * @author wduck
 */
public class StudentFactory extends PersonFactoryMethod{

    @Override
    public Person create() {
        Student student = (Student)dataIngress(); 
        return student;
    }

    @Override
    public Person dataIngress() {
        // AquI INGRESAR INFO
        Student s = new Student("PEPITO", "PEREZ ERAS",  "1104592656", 
                SocialEconomicLevel.MEDIUM);
        return s;
    }
}
