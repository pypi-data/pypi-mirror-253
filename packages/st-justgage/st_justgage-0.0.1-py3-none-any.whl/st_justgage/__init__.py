import streamlit.components.v1 as components
import os

import logging


_RELEASE = True


if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "st_justgage",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3000",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_justgage", path=build_dir)

                                     
def st_justgage(value: float,second_value:float, min_value: int, max_value: int, title: str=None, title_fontsize=20,title_color=None, key: str = None, customCSS: str = "",
    id: str = "",second_pointer =True, width = None, height = None,pointer = True,counter = True, gaugeWidthScale = 0.4, valueFontColor = 'Black', valueFontFamily = "Arial",
    symbol = "",minTxt = False,maxTxt = False,reverse = False,textRenderer = None,gaugeColor = '#ECEAE9',label = "",labelFontColor = "#b3b3b3",
    shadowOpacity = 0.2,shadowSize = 5,shadowVerticalOffset = 3,levelColors = ["#44546a"], startAnimationTime = 700,
    startAnimationType = ">",refreshAnimationTime = 700,refreshAnimationType ="<>",donutStartAngle = 90,valueMinFontSize = 50,labelMinFontSize = 10,
    minLabelMinFontSize = 15,maxLabelMinFontSize = 15,hideValue = False,hideMinMax = False,showInnerShadow = True,humanFriendly = False,noGradient = False,
    donut = False,differential = False,relativeGaugeSize = False,decimals = 0,customSectors = {},formatNumber = False,
    pointerOptions = {},displayRemaining = False
):
    """
    # https://github.com/toorshia/justgage#options
    Erstellt eine JustGage-Anzeige, ein anpassbares Gauge-Instrument.
    Parameter
    ----------
    value : int
        Der aktuelle Wert, der auf dem Gauge angezeigt wird.
    min_value : int
        Der minimale Wert des Gauge.
    max_value : int
        Der maximale Wert des Gauge.
    title : str, optional
        Der Titel des Gauge.
    title_fontsize : int, optional
        Die Schriftgröße des Titels.
    title_color : str, optional
        Die Schriftfarbe des Titels.
    key : str, optional
        Ein eindeutiger Schlüssel für das Element.
    customCSS : str, optional
        Benutzerdefinierte CSS-Regeln zur weiteren Anpassung.
    id : str, optional
        Die HTML-Container-Element-ID.
    width : int, optional
        Die Breite des Gauge.
    height : int, optional
        Die Höhe des Gauge.
    valueFontColor : str, optional
        Die Schriftfarbe des Wertes.
    valueFontFamily : str, optional
        Die Schriftart des Wertes.
    symbol : str, optional
        Ein Symbol oder Text, der dem Wert hinzugefügt wird (z.B. '%').
    minTxt : bool, optional
        Min-Wert-Text, überschreibt 'min_value', wenn angegeben.
    maxTxt : bool, optional
        Max-Wert-Text, überschreibt 'max_value', wenn angegeben.
    reverse : bool, optional
        Min. und Max. umkehren
    textRenderer : callable, optional
        Eine Funktion, die den Text für den Gauge-Wert anpasst.
    gaugeWidthScale : float, optional
        Skalierungsfaktor für die Dicke des Gauge.
    gaugeColor : str, optional
        Die Hintergrundfarbe des Gauge.
    label : str, optional
        Ein zusätzliches Label, das unter dem Wert angezeigt wird.
    labelFontColor : str, optional
        Die Schriftfarbe des Labels.
    shadowOpacity : float, optional
        Die Deckkraft des Schattens im Gauge. 0 ~ 1
    shadowSize : int, optional
        Die Größe des Schattens im Gauge.
    shadowVerticalOffset : int, optional
        Der vertikale Offset des Schattens im Gauge.
    levelColors : list, optional
        Die Farben für die verschiedenen Bereiche des Gauge.
    startAnimationTime : int, optional
        Die Dauer der Startanimation in Millisekunden.
    startAnimationType : str, optional
        Der Animationstyp bei der Initialisierung (z.B. linear, >, <, bounce).
    refreshAnimationTime : int, optional
        Die Dauer der Aktualisierungsanimation in Millisekunden.
    refreshAnimationType : str, optional
        Der Animationstyp bei der Aktualisierung.
    donutStartAngle : int, optional
        Der Startwinkel des Gauge, wenn 'donut' aktiviert ist.
    valueMinFontSize : int, optional
        Die minimale Schriftgröße des Wertes.
    labelMinFontSize : int, optional
        Die minimale Schriftgröße des Labels.
    minLabelMinFontSize : int, optional
        Die minimale Schriftgröße des minimalen Wertes.
    maxLabelMinFontSize : int, optional
        Die minimale Schriftgröße des maximalen Wertes.
    hideValue : bool, optional
        Gibt an, ob der Wert versteckt werden soll.
    hideMinMax : bool, optional
        Gibt an, ob die minimalen und maximalen Werte versteckt werden sollen.
    showInnerShadow : bool, optional
        Gibt an, ob ein innerer Schatten angezeigt werden soll.
    humanFriendly : bool, optional
        Gibt an, ob Zahlen "human-friendly" formatiert werden sollen.
    noGradient : bool, optional
        Gibt an, ob der Farbverlauf deaktiviert werden soll.
    donut : bool, optional
        Gibt an, ob das Gauge als Donut dargestellt werden soll.
    differential : bool, optional
        Gibt an, ob nur die Differenz zum vorherigen Wert angezeigt werden soll.
    relativeGaugeSize : bool, optional
        Gibt an, ob die Größe des Gauge relativ zum umgebenden Element sein soll.
    counter : bool, optional
        Gibt an, ob eine Zähleranimation für die Werte verwendet werden soll.
    decimals : int, optional
        Die Anzahl der Dezimalstellen für den Wert.
    customSectors : dict, optional
        Ein Wörterbuch, das benutzerdefinierte Sektoren und deren Farben definiert.
    formatNumber : bool, optional
        Gibt an, ob Zahlen formatiert (z.B. mit Tausendertrennzeichen) angezeigt werden sollen.
    pointer : bool, optional
        Gibt an, ob ein Zeiger statt des Textes für den Wert verwendet werden soll.
    pointerOptions : dict, optional
        Optionen für die Anpassung des Zeigers.
    displayRemaining : bool, optional
        Gibt an, ob der verbleibende Wert (max - value) statt des tatsächlichen Wertes angezeigt werden soll.

    Returns
    -------
    component_value
        Der Wert der Komponente, normalerweise für interne Verwendung.
    """
    #Beispiel textRenderer 
    #text_renderer_func = """
    #function(value) {
    #return value + "%";
    #}
    #"""
    if pointerOptions == {}:
        pointerOptions = {
            'toplength': -15,
            'bottomlength': 10,
            'bottomwidth': 12,
            'color': 'black',
            'stroke': '#ffffff',
            'stroke_width': 3,
            'stroke_linecap': 'round'
        }

    component_value = _component_func(value=value,second_value=second_value,second_pointer=second_pointer, min_value=min_value, max_value=max_value,title=title,title_fontsize=title_fontsize,title_color=title_color, key=key, customCSS=customCSS,
        id=id, width = width, height = height, valueFontColor = valueFontColor, valueFontFamily = valueFontFamily,
        symbol = symbol,minTxt = minTxt,maxTxt = maxTxt,reverse = reverse,
        textRenderer = textRenderer,gaugeWidthScale = gaugeWidthScale,gaugeColor = gaugeColor,label = label,labelFontColor = labelFontColor,
        shadowOpacity = shadowOpacity,shadowSize = shadowSize,shadowVerticalOffset = shadowVerticalOffset,levelColors = levelColors,startAnimationTime = startAnimationTime,
        startAnimationType = startAnimationType,refreshAnimationTime = refreshAnimationTime,refreshAnimationType = refreshAnimationType,
        donutStartAngle = donutStartAngle,valueMinFontSize = valueMinFontSize,labelMinFontSize = labelMinFontSize,
        minLabelMinFontSize = minLabelMinFontSize,maxLabelMinFontSize = maxLabelMinFontSize,hideValue = hideValue,hideMinMax = hideMinMax,
        showInnerShadow = showInnerShadow,humanFriendly = humanFriendly,noGradient = noGradient,
        donut = donut,differential = differential,relativeGaugeSize = relativeGaugeSize,counter = counter,decimals = decimals,customSectors = customSectors,formatNumber = formatNumber,
        pointer = pointer,pointerOptions = pointerOptions,displayRemaining = displayRemaining
    )
    
    # Additional customization logic can be added here
    
    return component_value
