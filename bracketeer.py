def bracket(all64, all32, all16, all8, final_four, finals, winner):
    east64 = all64['East']
    east32 = all32['East']
    east16 = all16['East']
    east8 = all8['East']
    west64 = all64['West']
    west32 = all32['West']
    west16 = all16['West']
    west8 = all8['West']
    midwest64 = all64['Midwest']
    midwest32 = all32['Midwest']
    midwest16 = all16['Midwest']
    midwest8 = all8['Midwest']
    south64 = all64['South']
    south32 = all32['South']
    south16 = all16['South']
    south8 = all8['South']
    out = f"""{east64[0][0][:3]}                                                                 {south64[0][0][:3]}
    {east32[0][0][:3]}                                                         {south32[0][0][:3]}
{east64[0][1][:3]}    \\                                                       /    {south64[0][1][:3]}
        {east16[0][0][:3]}                                                 {south16[0][0][:3]}
{east64[1][0][:3]}    /   \\                                               /   \\    {south64[1][0][:3]}
    {east32[0][1][:3]}     \\                                             /     {south32[0][1][:3]}
{east64[1][1][:3]}          \\                                           /          {south64[1][1][:3]}
              {east8[0][0][:3]}                                     {south8[0][0][:3]}
{east64[2][0][:3]}          /   \\                                   /   \\          {south64[2][0][:3]}  
    {east32[1][0][:3]}     /     \\                                 /     \\     {south32[1][0][:3]}
{east64[2][1][:3]}    \\   /       \\                               /       \\   /    {south64[2][1][:3]}
        {east16[0][1][:3]}         \\                             /         {south16[0][1][:3]}
{east64[3][0][:3]}    /             \\                           /             \\    {south64[3][0][:3]}
    {east32[1][1][:3]}               \\                         /               {south32[1][1][:3]} 
{east64[3][1][:3]}                    \\                       /                    {south64[3][1][:3]}
                        {final_four['East'][:3]}                 {final_four['South'][:3]}
{east64[4][0][:3]}                    /   \\               /   \\                    {south64[4][0][:3]}
    {east32[2][0][:3]}               /     |             |     \\               {south32[2][0][:3]}
{east64[4][1][:3]}    \\             /      |             |      \\             /    {south64[4][1][:3]}
        {east16[1][0][:3]}         /       |             |       \\         {south16[1][0][:3]}
{east64[5][0][:3]}    /   \\       /        |             |        \\       /   \\    {south64[5][0][:3]}
    {east32[2][1][:3]}     \\     /         |             |         \\     /     {south32[2][1][:3]}   
{east64[5][1][:3]}          \\   /          |             |          \\   /          {south64[5][1][:3]}
              {east8[0][1][:3]}          /               \\          {south8[0][1][:3]}
{east64[6][0][:3]}          /            /                 \\            \\          {south64[3][0][:3]}
    {east32[3][0][:3]}     /            /                   \\            \\     {south32[3][0][:3]}
{east64[6][1][:3]}    \\   /            /                     \\            \\   /    {south64[6][1][:3]}
        {east16[1][1][:3]}            /                       \\            {south16[1][1][:3]}
{east64[7][0][:3]}    /              |                         |              \\    {south64[7][0][:3]}
    {east32[3][1][:3]}               |                         |               {south32[3][1][:3]}
{east64[7][1][:3]}                    \\                       /                    {south64[7][1][:3]}
                        {finals[0][:3]}                 {finals[1][:3]}
{west64[0][0][:3]}                    /   \\               /   \\                    {midwest64[0][0][:3]}
    {west32[0][0][:3]}               |     \\             /     |               {midwest32[0][0][:3]}
{west64[0][1][:3]}    \\              |      \\           /      |              /    {midwest64[0][1][:3]}
        {west16[0][0][:3]}            \\       Champion:       /             {midwest16[0][0][:3]}
{west64[1][0][:3]}    /   \\            \\       ! {winner[:3]} !       /            /   \\    {midwest64[1][0][:3]}
    {west32[0][1][:3]}     \\            \\                   /            /     {midwest32[0][1][:3]}
{west64[1][1][:3]}          \\            \\                 /            /          {midwest64[1][1][:3]}
              {west8[0][0][:3]}          \\               /          {midwest8[0][0][:3]}
{west64[2][0][:3]}          /   \\          |             |          /   \\          {midwest64[2][0][:3]}  
    {west32[1][0][:3]}     /     \\         |             |         /     \\     {midwest32[1][0][:3]}
{west64[2][1][:3]}    \\   /       \\        |             |        /       \\   /    {midwest64[2][1][:3]}
        {west16[0][1][:3]}         \\       |             |       /         {midwest16[0][1][:3]}
{west64[3][0][:3]}    /             \\      |             |      /             \\    {midwest64[3][0][:3]}
    {west32[1][1][:3]}               \\     |             |     /               {midwest32[1][1][:3]} 
{west64[3][1][:3]}                    \\   /               \\   /                    {midwest64[3][1][:3]}
                        {final_four['West'][:3]}                 {final_four['Midwest'][:3]}
{west64[4][0][:3]}                    /                       \\                    {midwest64[4][0][:3]}
    {west32[2][0][:3]}               /                         \\               {midwest32[2][0][:3]}
{west64[4][1][:3]}    \\             /                           \\             /    {midwest64[4][1][:3]}
        {west16[1][0][:3]}         /                             \\         {midwest16[1][0][:3]}
{west64[5][0][:3]}    /   \\       /                               \\       /   \\    {midwest64[5][0][:3]}
    {west32[2][1][:3]}     \\     /                                 \\     /     {midwest32[2][1][:3]}   
{west64[5][1][:3]}          \\   /                                   \\   /          {midwest64[5][1][:3]}
              {west8[0][1][:3]}                                     {midwest8[0][1][:3]}
{west64[6][0][:3]}          /                                           \\          {midwest64[3][0][:3]}
    {west32[3][0][:3]}     /                                             \\     {midwest32[3][0][:3]}
{west64[6][1][:3]}    \\   /                                               \\   /    {midwest64[6][1][:3]}
        {west16[1][1][:3]}                                                 {midwest16[1][1][:3]}
{west64[7][0][:3]}    /                                                       \\    {midwest64[7][0][:3]}
    {west32[3][1][:3]}                                                         {midwest32[3][1][:3]}
{west64[7][1][:3]}                                                                 {midwest64[7][1][:3]}"""
    print(out)