package project.poo;

import java.time.LocalDate;

import project.poo.dominio.Bootcamp;
import project.poo.dominio.Curso;
import project.poo.dominio.Dev;
import project.poo.dominio.Mentoria;

public class ProjectPOO {

    public static void main(String[] args) {
        Curso curso1 = new Curso();
        curso1.setTitulo("Curso Java");
        curso1.setDescricao("descrição do curso de Java");
        curso1.setCargaHoraria(8);
        
        Curso curso2 = new Curso();
        curso2.setTitulo("Curso Java focado em POO");
        curso2.setDescricao("descrição do curso de Java focado em POO");
        curso2.setCargaHoraria(18);
        
        Mentoria ment = new Mentoria();
        ment.setTitulo("Mentoria do Java");
        ment.setDescricao("descrição da mentoria do Java");
        ment.setData(LocalDate.now());

        Bootcamp boot = new Bootcamp();
        boot.setNome("Bootcamp Java Developer");
        boot.setDescricao("Descrição do Bootcamp de Java Developer");
        boot.getConteudos().add(curso1);
        boot.getConteudos().add(curso2);
        boot.getConteudos().add(ment);

        Dev dev = new Dev();
        dev.setNome("Ana");
        dev.inscreverBootcamp(boot);
        System.out.println("Conteúdos inscritos: " + dev.getConteudosInscritos());
        dev.progredir();
        System.out.println("Conteúdos inscritos: " + dev.getConteudosInscritos());
        System.out.println("Conteúdos concluídos: " + dev.getConteudosFinalizados());
        System.out.println("XP: " + dev.calcularTotalXp());

        System.out.println("-=-=-=-=-=-=-=-=-=-");

        Dev dev1 = new Dev();
        dev1.setNome("Paula");
        dev1.inscreverBootcamp(boot);
        System.out.println("Conteúdos inscritos: " + dev1.getConteudosInscritos());
        dev1.progredir();
        dev1.progredir();
        dev1.progredir();
        System.out.println("Conteúdos inscritos: " + dev1.getConteudosInscritos());
        System.out.println("Conteúdos concluídos: " + dev1.getConteudosFinalizados());
        System.out.println("XP: " + dev1.calcularTotalXp());
    }
    
}
