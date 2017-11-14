/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package k9helper;

/**
 *
 * @author Tim
 */
public class Quote {
    private String quote, speaker;

    public Quote(String quote, String speaker) {
        this.quote = quote;
        this.speaker = speaker;
    }

    
    public String getQuote() {
        return quote;
    }

    public void setQuote(String quote) {
        this.quote = quote;
    }

    public String getSpeaker() {
        return speaker;
    }

    public void setSpeaker(String speaker) {
        this.speaker = speaker;
    }
    
    
}
