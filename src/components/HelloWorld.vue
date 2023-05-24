<template>
  
  <div
    class="d-flex flex-column justify-content-right align-items-center"
    style="height: 80vh"
    
  >
    <div class="p-2">
      <h1 v-if="!APIResult.length">Enter Car data to make prediction</h1>
      <h1 v-else style="font-size:40px">{{ APIResult }}</h1>
    </div>
    <div class="p-2">
      <form @submit.prevent>
        <div class="form-row" style="max-width:100000px">

          <div class ="form-group col-md-3" >   
            
            <label for="a" style="float:left;">Car Brand : </label>
            <select
              v-model.trim="winedata.a"
              class="from control" style="float:left;"
              id="car_name"
            >
                <option value="0"  selected>Audi </option>
                <option value="1"  selected>BMW </option>
                <option value="2"  selected>Chevrolet </option>
                <option value="3"  selected>Datsun </option>
                <option value="4"  selected>Fiat </option>
                <option value="5"  selected>Ford </option>
                <option value="6"  selected>Honda </option>
                <option value="7"  selected>Hyundai </option>
                <option value="8"  selected>Mahindra </option>
                <option value="9" selected>Maruti </option>
                <option value="10" selected>Mercedes-Benz </option>
                <option value="11" selected>Nissan </option>
                <option value="12" selected>Renault </option>
                <option value="13" selected>Skoda </option>
                <option value="14" selected>Tata </option>
                <option value="15" selected>Toyota </option>
                <option value="16" selected>Volkswagen</option>
            </select>
            <pre>

            </pre>
          </div>
          <div class="form-group col-md-3">
            <label for="a">Model  Name   =    </label>
            <select
              v-model.trim="winedata.b"
              class="from control"
              id="model_name">
            >  
            <option value = "0" selected>	 A-Star   	</option>
            <option value = "1" selected>	 A4       	</option>
            <option value = "2" selected>	 A5       	</option>
            <option value = "3" selected>	 A6       	</option>
            <option value = "4" selected>	 A8       	</option>
            <option value = "5" selected>	 Accent   	</option>
            <option value = "6" selected>	 Accord   	</option>
            <option value = "7" selected>	 Alto     	</option>
            <option value = "8" selected>	 Altroz   	</option>
            <option value = "9" selected>	 Alturas  	</option>
            <option value = "10" selected>	 Amaze    	</option>
            <option value = "11" selected>	 Ameo     	</option>
            <option value = "12" selected>	 Aria     	</option>
            <option value = "13" selected>	 Aspire   	</option>
            <option value = "14" selected>	 Aveo     	</option>
            <option value = "15" selected>	 Avventura	</option>
            <option value = "16" selected>	 B-Class  	</option>
            <option value = "17" selected>	 BR-V     	</option>
            <option value = "18" selected>	 BRV      	</option>
            <option value = "19" selected>	 Baleno   	</option>
            <option value = "20" selected>	 Beat     	</option>
            <option value = "21" selected>	 Bolero   	</option>
            <option value = "22" selected>	 Bolt     	</option>
            <option value = "23" selected>	 Brio     	</option>
            <option value = "24" selected>	 C-Class  	</option>
            <option value = "25" selected>	 CR-V     	</option>
            <option value = "26" selected>	 Camry    	</option>
            <option value = "27" selected>	 Captiva  	</option>
            <option value = "28" selected>	 Captur   	</option>
            <option value = "29" selected>	 Celerio  	</option>
            <option value = "30" selected>	 Ciaz     	</option>
            <option value = "31" selected>	 City     	</option>
            <option value = "32" selected>	 Civic    	</option>
            <option value = "33" selected>	 Classic  	</option>
            <option value = "34" selected>	 Corolla  	</option>
            <option value = "35" selected>	 Creta    	</option>
            <option value = "36" selected>	 CrossPolo	</option>
            <option value = "37" selected>	 Cruze    	</option>
            <option value = "38" selected>	 Duster   	</option>
            <option value = "39" selected>	 E-Class  	</option>
            <option value = "40" selected>	 EON      	</option>
            <option value = "41" selected>	 EcoSport 	</option>
            <option value = "42" selected>	 Ecosport 	</option>
            <option value = "43" selected>	 Eeco     	</option>
            <option value = "44" selected>	 Elantra  	</option>
            <option value = "45" selected>	 Elite    	</option>
            <option value = "46" selected>	 Endeavour	</option>
            <option value = "47" selected>	 Enjoy    	</option>
            <option value = "48" selected>	 Ertiga   	</option>
            <option value = "49" selected>	 Esteem   	</option>
            <option value = "50" selected>	 Estilo   	</option>
            <option value = "51" selected>	 Etios    	</option>
            <option value = "52" selected>	 Evalia   	</option>
            <option value = "53" selected>	 F500     	</option>
            <option value = "54" selected>	 Fabia    	</option>
            <option value = "55" selected>	 Fiesta   	</option>
            <option value = "56" selected>	 Figo     	</option>
            <option value = "57" selected>	 Fluence  	</option>
            <option value = "58" selected>	 Fortuner 	</option>
            <option value = "59" selected>	 Freestyle	</option>
            <option value = "60" selected>	 Fusion   	</option>
            <option value = "61" selected>	 GL-Class 	</option>
            <option value = "62" selected>	 GLS      	</option>
            <option value = "63" selected>	 GO       	</option>
            <option value = "64" selected>	 Getz     	</option>
            <option value = "65" selected>	 Grand    	</option>
            <option value = "66" selected>	 Grande   	</option>
            <option value = "67" selected>	 Gypsy    	</option>
            <option value = "68" selected>	 Harrier  	</option>
            <option value = "69" selected>	 Hexa     	</option>
            <option value = "70" selected>	 Ignis    	</option>
            <option value = "71" selected>	 Ikon     	</option>
            <option value = "72" selected>	 Indica   	</option>
            <option value = "73" selected>	 Indigo   	</option>
            <option value = "74" selected>	 Ingenio  	</option>
            <option value = "75" selected>	 Innova   	</option>
            <option value = "76" selected>	 Jazz     	</option>
            <option value = "77" selected>	 Jeep     	</option>
            <option value = "78" selected>	 Jetta    	</option>
            <option value = "79" selected>	 KUV      	</option>
            <option value = "80" selected>	 KWID     	</option>
            <option value = "81" selected>	 Kicks    	</option>
            <option value = "82" selected>	 Koleos  	</option>
            <option value = "83" selected>	 Laura   	</option>
            <option value = "84" selected>	 Linea   	</option>
            <option value = "85" selected>	 Lodgy   	</option>
            <option value = "86" selected>	 M-Class 	</option>
            <option value = "87" selected>	 M800    	</option>
            <option value = "88" selected>	 Manza   	</option>
            <option value = "89" selected>	 Marazzo 	</option>
            <option value = "90" selected>	 Micra   	</option>
            <option value = "91" selected>	 Mobilio 	</option>
            <option value = "92" selected>	 Nano    	</option>
            <option value = "93" selected>	 New-C   	</option>
            <option value = "94" selected>	 Nexon   	</option>
            <option value = "95" selected>	 NuvoSpor	</option>
            <option value = "96" selected>	 Octavia 	</option>
            <option value = "97" selected>	 Omni    	</option>
            <option value = "98" selected>	 Optra   	</option>
            <option value = "99" selected>	 Palio   	</option>
            <option value = "100" selected>	 Passat  	</option>
            <option value = "101" selected>	 Polo    	</option>
            <option value = "102" selected>	 Pulse   	</option>
            <option value = "103" selected>	 Punto   	</option>
            <option value = "104" selected>	 Q3      	</option>
            <option value = "105" selected>	 Q5      	</option>
            <option value = "106" selected>	 Q7      	</option>
            <option value = "107" selected>	 Qualis  	</option>
            <option value = "108" selected>	 Quanto  	</option>
            <option value = "109" selected>	 RS7     	</option>
            <option value = "110" selected>	 Rapid   	</option>
            <option value = "111" selected>	 RediGO  	</option>
            <option value = "112" selected>	 Renault 	</option>
            <option value = "113" selected>	 Ritz    	</option>
            <option value = "114" selected>	 S-Class 	</option>
            <option value = "115" selected>	 S-Cross 	</option>
            <option value = "116" selected>	 S-Presso	</option>
            <option value = "117" selected>	 SX4     	</option>
            <option value = "118" selected>	 Safari  	</option>
            <option value = "119" selected>	 Sail    	</option>
            <option value = "120" selected>	 Santa   	</option>
            <option value = "121" selected>	 Santro  	</option>
            <option value = "122" selected>	 Scala   	</option>
            <option value = "123" selected>	 Scorpio 	</option>
            <option value = "124" selected>	 Sonata  	</option>
            <option value = "125" selected>	 Spacio  	</option>
            <option value = "126" selected>	 Spark   	</option>
            <option value = "127" selected>	 Sumo    	</option>
            <option value = "128" selected>	 Sunny   	</option>
            <option value = "129" selected>	 Superb  	</option>
            <option value = "130" selected>	 Supro   	</option>
            <option value = "131" selected>	 Swift   	</option>
            <option value = "132" selected>	 TUV     	</option>
            <option value = "133" selected>	 Tavera  	</option>
            <option value = "134" selected>	 Terrano 	</option>
            <option value = "135" selected>	 Thar    	</option>
            <option value = "136" selected>	 Tiago   	</option>
            <option value = "137" selected>	 Tigor   	</option>
            <option value = "138" selected>	 Triber  	</option>
            <option value = "139" selected>	 Tucson  	</option>
            <option value = "140" selected>	 Vento   	</option>
            <option value = "141" selected>	 Venture 	</option>
            <option value = "142" selected>	 Venue   	</option>
            <option value = "143" selected>	 Verito  	</option>
            <option value = "144" selected>	 Verna   	</option>
            <option value = "145" selected>	 Vitara  	</option>
            <option value = "146" selected>	 WR-V    	</option>
            <option value = "147" selected>	 Wagon   	</option>
            <option value = "148" selected>	 Winger  	</option>
            <option value = "149" selected>	 X-Trail 	</option>
            <option value = "150" selected>	 X1      	</option>
            <option value = "151" selected>	 X3      	</option>
            <option value = "152" selected>	 X5      	</option>
            <option value = "153" selected>	 X7      	</option>
            <option value = "154" selected>	 XUV300  	</option>
            <option value = "155" selected>	 XUV500  	</option>
            <option value = "156" selected>	 Xcent   	</option>
            <option value = "157" selected>	 Xenon   	</option>
            <option value = "158" selected>	 Xylo    	</option>
            <option value = "159" selected>	 Yaris   	</option>
            <option value = "160 " selected	> Yeti    	</option>
            <option value = "161" selected>	 Zen     	</option>
            <option value = "162" selected>	 Zest    	</option>
            <option value = "163" selected>	 i10     	</option>
            <option value = "164" selected>	 i20     	</option>
            <option value = "165" selected>	 redi-GO 	</option>


            
            </select>
          </div>
          
          <div class="form-group col-md-3">
            <label class="col-12 px-0" for="c" style="float:left;">Kms Driven    =  </label>
            <input
              class="form-control" style="float:left;"
              v-model.trim="winedata.c"
              type="number"
              id="c"
            />
            <pre>
              
            </pre>
          </div>
          <div class="form-group col-md-3">
            <label class="col-12 px-0" for="d" >No of Years   =   </label>
            <input
              class="form-control"
              v-model.trim="winedata.d"
              type="number"
              id="d"
            />
            <pre>
              
            </pre>
          </div>
          <div class="form-group col-md-3">
            <label class="col-12 px-0" for="e" style="float:left;">Fuel Type   =   </label>
            
            <select
              v-model.trim="winedata.e" style="float:left;"
              class="from control"
              id="d"
             >
              <option value="1" selected>Petrol</option>
              <option value="0" selected>Diesel</option>

            </select>
            <pre>
              
            </pre>
            
          </div>
          <div class="form-group col-md-3">
            <label class="col-12 px-0" for="f" style="float:center;">Transmission   =   </label>
            <select
              v-model.trim="winedata.f" style="float:center;"
              class="from control"
              id="d"
             >
              <option value="1" selected>Manual   </option>
              <option value="0" selected>Automatic</option>

            </select>
            <pre>
              
            </pre>
          </div>
          <div class="form-group col-md-4">
            <label class="col-12 px-0" for="g" style="float:left;" >Owner   =   </label>
            <select
              v-model.trim="winedata.g" style="float:left;"
              class="from control"
              id="d"
             >
              <option value="0" selected>First Owner         </option>
              <option value="2" selected>Second Owner       </option>
              <option value="4" selected>Third Owner         </option>
              <option value="1" selected>Fourth & Above Owner     </option>
              <option value="3" selected>Test Drive Car     </option>

            </select>
            <pre>
              
            </pre>
          
            
          </div>
          <button
            @click="predict"
            type="button"
            class="btn btn-primary btn-lg btn-block"
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import "./style.css";
import { getAPI } from "@/axios";
export default {
  name: "ModelView",
  data() {
    return {
      winedata: {
        a: "",
        b: "",
        c: "",
        d: "",
        e: "",
        f: "",
        g: ""
       
      },
      APIResult: []
    };
  },
  methods: {
    predict() {
      getAPI
        .get("/model", {
          params: {

           

            Car_Name: this.winedata.a,
            Car_Model: this.winedata.b,
            Kms_Driven: this.winedata.c,
            No_of_Years: this.winedata.d,
            Fuel_Type: this.winedata.e,
            Transmission: this.winedata.f,
            Owner: this.winedata.g,


           
          }
        })
        .then(response => {
          console.log("Recieved data successfully");
          this.APIResult = response.data;
          console.log(response.data);
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>

<style>
</style>

