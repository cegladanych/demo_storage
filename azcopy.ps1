$sourceuri = ""
$destinationuri = ""
$sourcesas = ""
$destinationsas = ""

$source = "$sourceuri$sourcesas"
$destination = "$destinationuri$destinationsas"

$csvpath = 'C:\Users\admin\Downloads\projectx2.csv'

$csvobject = Import-CSV $csvpath

#Czytamy plik csv
$csvheader = (Get-Content $csvpath | Select-Object -First 1)
$delimeter = ",";
$columnheader = $csvheader -Split $delimeter

foreach($item in $csvobject)
{
    $filename = "$($item.$($columnheader[1]))$.tiff"
    $source = "$sourceuri$filename$sourcesas"
    $destination = "$destinationuri$filename$destinationsas"
    & ".\azcopy.exe" cp "$source" "$destination" --recursive=TRUE
    Write-Host "File name = $filename"
}

