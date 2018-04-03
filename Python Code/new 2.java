import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


public class Solution {
    
    public static class Event{
        int id;
        int xE;
        int yE;
        PriorityQueue<Integer> tickets;
        
        Event(int id, int xE,int yE,String[] ticketsArr){
            this.id = id;
            this.xE = xE;
            this.yE = yE;
            tickets = new PriorityQueue<Integer>();
            //tickets.addAll(Arrays.asList());
            
            for(String t : ticketsArr){
                tickets.add(Integer.parseInt(t));
            }
            
        }
    }
    
    public static class Buyer{
        int xB;
        int yB;
    }
    public static void main(String args[] ) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
        List<Event> eventsList = new LinkedList<>();
        List<Buyer> buyersList = new LinkedList<>();
        Scanner scan = new Scanner(System.in);
        
        int sizeOfWorld = Integer.parseInt(scan.nextLine());
        int numberOfEvents = Integer.parseInt(scan.nextLine());
        while(numberOfEvents > 0){
            String event = scan.nextLine();
            // TODO: you will need to parse and store the events 
            String[] events = event.split(" ");
            Event e = new Event(Integer.parseInt(events[0]),Integer.parseInt(events[1]),Integer.parseInt(events[2]),Arrays.copyOfRange(events,3,events.length));
            eventsList.add(e);
            numberOfEvents--;
        }
        
        int numberOfBuyers = Integer.parseInt(scan.nextLine());
        while(numberOfBuyers > 0){
            String buyer = scan.nextLine();
            // TODO: you will need to parse and store the buyers 
            String[] buyers = buyer.split(" ");
            Buyer b = new Buyer(Integer.parseInt(buyers[0]),Integer.parseInt(buyers[1]));
            //buyersList(b);
            List<Event> minDistEvents = findClosest(b,eventsList);
            
            if(minDistEvents.size() == 1){
                System.println(minDistEvents.get(0).id,minDistEvents.get(0).tickets.poll());
                if(minDistEvents.get(0).tickets.isEmpty() ){
                    minDistEvents.get(0).xE= Integer.MAX_VALUE;
                    minDistEvents.get(0).yE= Integer.MAX_VALUE;
                }
            }
            else{
                int min = Integer.MAX_VALUE;
                Event minEvent;
                for(Event e : minDistEvents){
                    if(e.tickets.peek() < min){
                        min = e.tickets.peek();
                        minEvent = e;
                    }
                }
                System.out.println(minEvent.id, minEvent.tickets.poll());
                if(minEvent.tickets.isEmpty() ){
                    minEvent.xE= Integer.MAX_VALUE;
                    minEvent.yE= Integer.MAX_VALUE;
                }
            }
            numberOfBuyers--;
        }

        // The solution to the first sample above would be to output the following to console:
        // (Obviously, your solution will need to figure out the output and not just hard code it)
        System.out.println("2 50");
    }
    
    public static List<Integer> findClosest(Buyer b,List<Event> eventsList){
        List<Event> minDistEvents = new ArrayList<>();
        int distance = new int[eventsList.size()];
        int i = 0;
        for(Event e: eventsList){
            distance[i] = ManhattanDistance(b,e);
            i++;
        }
        
        int minimum = distance[0]; 
       // int minValueCounter = 0;
        int minId = 0;
        for (int i = 0; i < distance.length; i++) {
            if (distance[i] < minimum){
                //minId = i; 
                minimum = distance[i];
                minDistEvents.removeAll(minDistEvents);
                minDistEvents.add(eventsList.get(i));
            }
            else if (distance[i] == minimum)  {
                 minDistEvents.add(eventsList.get(i));               
            }
            
        }
        
        return minDistEvents;
    }
    
    public static int ManhattanDistance(Buyer b,Event e){
        return Math.abs(e.xE-b.xB) + Math.abs(e.yE- b.yB); 
    }
}