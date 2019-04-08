 class PrimeNumber {

    /**
     * @param args the command line arguments
     */
    public int totalThread = 1, inputNumber =1003;
     // long start;
    public  static void main(String[] args) {
        // System.out.println(args[1]);
        PrimeNumber pn = new PrimeNumber();
        pn.totalThread = Integer.parseInt(args[1]);
        pn.inputNumber = Integer.parseInt(args[0]);
        pn.startThread();
        
    }

    private void startThread(){
        long start = System.nanoTime(); 
         for(int a=0; a<totalThread; a++){
            PrimeThread pt = new PrimeThread(a+1, totalThread, inputNumber, start);
            pt.start();
        }
    }
    
    // private boolean prime(int initNumber){
    //     System.out.println((inputNumber/totalThread));
    //     for(int i =0; i<(inputNumber/totalThread);i++){
    //         int modCalculation = initNumber + (totalThread * i);
    //         if (modCalculation <=3){
    //            // return true;
    //         } else if(modCalculation < inputNumber) {
    //             System.out.println(inputNumber + " "+ modCalculation);
    //             if( (inputNumber % modCalculation) == 0){
    //                 long end = System.nanoTime(); 
    //                 System.out.println((end - start) + " nano");
    //                 return false;
    //             } 
    //         }

    //     }
    //     return true;
    // }
    
}

class PrimeThread implements Runnable {
   private Thread t;
   private int initNumber, totalThread, inputNumber;
   private long start;
   
   PrimeThread( int initNumber, int totalThread, int inputNumber, long start) {
        this.initNumber = initNumber;
        this.totalThread = totalThread;
        this.inputNumber = inputNumber;
        this.start = start;
   }
   
   public void run() {
      // System.out.println(this.prime(initNumber));
    this.prime(initNumber);
   }

   private boolean prime(int initNumber){
        // System.out.println((inputNumber/totalThread));
        for(int i =0; i<(inputNumber/totalThread);i++){
            int modCalculation = initNumber + (totalThread * i);
            if (modCalculation <=3){
               // return true;
            } else if(modCalculation < inputNumber) {
                // System.out.println(inputNumber + " "+ modCalculation);
                if( (inputNumber % modCalculation) == 0){
                    long end = System.nanoTime(); 
                    System.out.println(modCalculation + " " +(end - start) + " nano");
                    return false;
                } 
            }

        }
        return true;
    }
   
   public void start () {
      System.out.println("Starting " +  initNumber );
      if (t == null) {
         t = new Thread (this, String.valueOf(initNumber));
         t.start ();
      }
   }
}