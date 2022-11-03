using System;
using static System.Net.Mime.MediaTypeNames;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using static System.Net.WebRequestMethods;


class Init
{
    static void Main()
    {
        string name;
        int frames;

        Console.WriteLine("Ingrese el nombre del archivo: ");
        name =Console.ReadLine();

        Console.WriteLine("Ingrese los frames de la imagen: ");
        frames = int.Parse(Console.ReadLine());

        Console.Clear();

        string path = Path.GetFullPath(@"..\..\Source\"+name+".txt");
        while (true) 
        { 
            using (FileStream fs = new FileStream(path, FileMode.Open, FileAccess.Read))
            {
                using (StreamReader sr = new StreamReader(fs))
                {
                    while (!sr.EndOfStream)
                    {
                        string line = sr.ReadLine();
                        if (line=="break")
                        {
                            Thread.Sleep(frames);
                            Console.Clear();
                            continue;
                        }
                        Console.WriteLine(line);
                    }
                }
            }
        }
    }
}
