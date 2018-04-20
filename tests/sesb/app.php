<?php


class tag //Можно было реализовать и наследованием классов или ваще не реализовывать, но вот увлёкся.
{
    private $include;
    private $class;
    private $params;
    private $name;
    private $id;
    private $double;

    public function __construct($name = null, $double = false, $id = null, $class=null, $params = [], $include = [])
    {
        $this->name=$name;
        $this->double=$double;
        if ($class) {
            $this->class=$class;
        }
        if ($id) {
            $this->id=$id;
        }
        $this->params=$params;
        $this->include=$include;
    }
    public function insertTAG($tag, $id=null, $class=null)
    {
        if (!isset($id) && !isset($class)) {
            $this->include[]=$tag;
            return;
        } else {
            foreach ($this->include as $oldTag) {
                $oldTag->insertTAG($tag, $id, $class);
            }
            if (($this->id == $id && $this->class == $class) or ($this->id == $id && $this->class == null) or ($this->id == null && $this->class == $class)) {
                $this->include[]=$tag;
            }
        }
    }
    private function brackets($str, $type='open')
    {
        if ($type=='open') {
            return '<'.$str.'>';
        } elseif ($type == 'close') {
            return '</'.$str.'>';
        }
    }

    private function quotes($str, $single=true)
    {
        if ($single == true) {
            return "'".$str."'";
        }
        return '"'.$str.'"';
    }

    public function toString()
    {
        if ($this->name == null) {
            return $this->include[0];
        }
        $include='';
        $params=[];
        $params[0]=$this->name;
        if ($this->class) {
            $params[]='class='.$this->quotes($this->class);
        }
        if ($this->id) {
            $params[]='id='.$this->quotes($this->id);
        }
        if (is_array($this->include)) {
            foreach ($this->include as $value) {
                $include.=$value->toString();
            }
        }
        if ($this->double) {
            $closing = $this->brackets($this->name, 'close');
        } else {
            $closing='';
        }
        foreach ($this->params as $key=>$value) {
            $params[]=$key.'='.$this->quotes($value);
        }

        return $this->brackets(implode(' ', $params)).$include.$closing;
    }

    public function insertParameter(array $param)
    {
        try {
            foreach ($this->param as $key=>$value) {
                $this->params[$key]=$value;
            }
            return true;
        } catch (Exception $e) {
            return false;
        }
    }


    public function getParams()
    {
        return $this->params;
    }
}



class tester
{
    private $POST=null;
    private $GET=null;
    private $HTML;
    public function __construct()
    {
        $File=fopen('main.html', 'r');
        $this->HTML = fread($File);
        fclose($File);
        if ($_POST['url']) {
            $this->POST=$_POST;
        } elseif ($_GET['url']) {
            $this->GET=$_GET;
        } else {
            echo 'ff';
        }
    }

    public function html()
    {
        $this->HTML;
    }

    public function start()
    {
        if ($_POST) {
        } else {
            $this->html();
        }
    }
}

class templator {




}

//$name = null, $double = false, $id = null, $class=null, $params = [], $include = []
$HL=new tag('html', true);
$body=new tag('body', true);
$img=new tag('img', false, null, null, ['src'=>'https://www.google.ru/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png']);
$app=new tag('a', true, 't1', 't2', ['href'=>'https://google.ru'], [$img]);

$body->insertTAG($app);
$HL->insertTAG($body);
print_r($HL->toString().PHP_EOL);


$options=[];
$txtPost=new tag(null,false,null,null,[],['POST']);
$txtGet=new tag(null,false,null,null,[],['GET']);
$options[]=new tag('option',true,null,null,['value'=>'post'],[$txtPost]);
$options[]=new tag('option',true,null,null,['value'=>'get'],[$txtGet]);
$select=new tag('select',true,null,null,['name'=>'method']);
foreach ($options as $option) {
  $select->insertTAG($option);
}

/*
<form action='app.php' method='post'>
  URL:
  <input name='url'></input><br>
  Method:
  <select name='method'>*/


  /*</select><br>
  <table>

    <tr>
      <td><input name='query1'></input>
      </td>
      <td><input name='data1'></input>
      </td>
    </tr>
    <tr>
      <td><input name='query2'></input>
      </td>
      <td><input name='data1'></input>
      </td>
    </tr>
    <tr>
      <td><input name='query3'></input>
      </td>
      <td><input name='data1'></input>
      </td>
    </tr>
    <tr>
      <td><input name='query4'></input>
      </td>
      <td><input name='data1'></input>
      </td>
    </tr>
    <tr>
      <td><input name='query5'></input>
      </td>
      <td><input name='data1'></input>
      </td>
    </tr>

  </table>
  <input type="submit" value="Опросить">
</form>











*/














?>
