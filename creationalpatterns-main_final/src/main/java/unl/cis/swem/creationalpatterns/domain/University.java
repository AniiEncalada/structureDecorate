package unl.cis.swem.creationalpatterns.domain;

public class University{
    //propiedades privadas de la clase
    private String name;
    private String address;            
    //1. Crear una instancia de la misma clase como estática y privada
    private static University UniversityActual;

    //2. Declarar el contructor de la clase como estático y privado
    //para que no pueda ser instanciada la clase directamente
    private University (String name, String address)
    {
        this.name=name;
        this.address=address;
    }

    //3. Crear un método público que permita crear la instancia de la clase
    //este método controlará que la instancia solo se cree la primera vez
    //si la instancia ya fue creada anteriormente devuelve la misma instancia anterior
    public static University getUniversity(String name, String address)
    {
        if (UniversityActual == null)
            UniversityActual = new University(name, address);
        return UniversityActual;
    }
        
    public void presentar() {

        System.out.println("============= DATOS University=========="); 
        System.out.println("CLASE: " + this.getClass().getName().toUpperCase());
        System.out.println("El nombre de la University es: " + name);  
        System.out.println("La dirección de la University es: " + address);  
    }

}
